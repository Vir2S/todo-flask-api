from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "thisissecret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////./todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(debug=True)
