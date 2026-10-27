from flask import Blueprint, render_template

web = Blueprint("web",__name__)

@web.route("/")
def t_home():
    return render_template("index.html")