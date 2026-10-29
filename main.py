from flask import Flask, render_template
from views.web.routes import web
from flask import g
import sqlite3

DATABASE = '/instance/users.db'

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

app = Flask(__name__)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

app.register_blueprint(web)

if __name__ == "__main__":
    app.run(debug=True)