from flask import Blueprint, render_template, request, abort
import requests as req
from db import Db_oject
import datetime as dt
import os
import secrets

web = Blueprint("web",__name__)

@web.route("/")
def t_home():
    return render_template("index.html")

@web.route("/telebot/<msg>")
def r_telebot(msg):
    TOKEN = 'MY TOKEN'
    chat_id = 'MY ID'
    message = msg
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    db = Db_oject()
    try:
        db.cur.execute(f"INSERT INTO logs (timestamp, msg) VALUES (?, ?)", [str(dt.datetime.now()), msg])
        db.con.commit()
        res = req.get(url)
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": f"{e}"}


WEBHOOK_SECRET = 'os.environ["TELEGRAM_WEBHOOK_SECRET"]'


@web.route("/telegram/webhook", methods=["POST"])
def telegram_webhook():
    # Comprueba que la petición contiene el secreto configurado.
    received_secret = request.headers.get(
        "X-Telegram-Bot-Api-Secret-Token", ""
    )
    if not secrets.compare_digest(received_secret, WEBHOOK_SECRET):
        abort(403)

    update = request.get_json(silent=True)
    if not isinstance(update, dict):
        abort(400)

    # Hay actualizaciones que no contienen mensajes de texto.
    message = update.get("message") or {}
    text = message.get("text")
    chat_id = message.get("chat", {}).get("id")

    if text is None or chat_id is None:
        return {"ok": True}

    db = Db_oject()
    try:
        db.cur.execute(
            "INSERT INTO logs (timestamp, msg) VALUES (?, ?)",
            [str(dt.datetime.now()), text],
        )
        db.con.commit()
    except Exception:
        pass

    return {"ok": True}