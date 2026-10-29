from flask import Blueprint, render_template
import requests as req
from db import Db_oject
import datetime as dt

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
