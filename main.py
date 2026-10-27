from flask import Flask, render_template
from views.web.routes import web

app = Flask(__name__)

app.register_blueprint(web)

if __name__ == "__main__":
    app.run(debug=True)