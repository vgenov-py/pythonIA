import datetime as dt
import os
import time
from openai import OpenAI
import requests
from db import Db_oject


def guardar_mensaje(chat_id, texto):
    print(f"Telegram [{chat_id}]: {texto}", flush=True)

    db = Db_oject()
    try:
        with db.con:
            db.con.execute(
                "INSERT INTO logs (timestamp, msg) VALUES (?, ?)",
                (str(dt.datetime.now()), texto),
            )
    finally:
        db.con.close()

    # Aquí puedes ejecutar otras acciones de tu aplicación.


def recibir_mensajes(app):
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    base_url = f"https://api.telegram.org/bot{token}"

    def llamar_telegram(method, payload):
        response = requests.post(
            f"{base_url}/{method}",
            json=payload,
            timeout=(10, 40),
        )
        data = response.json()

        if not data.get("ok"):
            raise RuntimeError(data.get("description", "Error de Telegram"))

        response.raise_for_status()
        return data["result"]

    offset = None
    webhook_eliminado = False

    while True:
        try:
            if not webhook_eliminado:
                llamar_telegram(
                    "deleteWebhook",
                    {"drop_pending_updates": False},
                )
                webhook_eliminado = True
                app.logger.info("Receptor de Telegram iniciado")

            updates = llamar_telegram(
                "getUpdates",
                {
                    "offset": offset,
                    "timeout": 30,
                    "allowed_updates": ["message"],
                },
            )

            for update in updates:
                message = update.get("message") or {}
                texto = message.get("text")
                chat_id = message.get("chat", {}).get("id")
                # IA INICIO
                if texto:
                    x = os.environ.get("OPENAI_KEY")
                    client = OpenAI(api_key=x)

                    response = client.responses.create(
                        model="gpt-4.1-mini",
                        input=texto,
                        max_output_tokens=50,
                    )

                    print(response.output_text)
                    TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
                    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={response.output_text}"
                    res = requests.get(url)
                # IA FIN
                if texto is not None and chat_id is not None:
                    with app.app_context():
                        guardar_mensaje(chat_id, texto)

                offset = update["update_id"] + 1

        except requests.RequestException:
            # Evita imprimir URLs que contienen el token.
            app.logger.warning("Error de conexión con Telegram")
            time.sleep(5)

        except Exception as error:
            app.logger.error("Error del receptor: %s", error)
            time.sleep(5)