from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config["SECRET_KEY"] = "thisissecret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    is_admin = db.Column(db.Boolean)


class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    is_completed = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)


@app.route("/user", methods=["GET"])
def get_all_users():
    return ""


@app.route("/user/<user_id>", methods=["GET"])
def get_user():
    return ""


@app.route("/user", methods=["POST"])
def create_user():
    return ""


@app.route("/user/user_id", methods=["PUT"])
def edit_user():
    return ""


@app.route("/user/user_id", methods=["DELETE"])
def delete_user():
    return ""


if __name__ == "__main__":
    app.run(debug=True)
