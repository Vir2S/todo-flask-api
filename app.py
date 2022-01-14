from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

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
    is_admin = db.Column(db.Boolean, default=False)


class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    is_completed = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)


@app.route("/user", methods=["GET"])
def get_all_users():
    users = User.query.all()

    context = []

    for user in users:
        user_data = {}
        user_data["public_id"] = user.public_id
        user_data["name"] = user.name
        user_data["is_admin"] = user.is_admin
        context.append(user_data)

    return jsonify({"users": context})


@app.route("/user/<public_id>", methods=["GET"])
def get_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({"message": "User not found!"})

    user_data = {}
    user_data["public_id"] = user.public_id
    user_data["name"] = user.name
    user_data["is_admin"] = user.is_admin

    return jsonify({"user": user_data})


@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()

    hashed_password = generate_password_hash(data["password"], method="sha256")

    new_user = User(
        public_id=str(uuid.uuid4()),
        name=data["name"],
        password=hashed_password,
        admin=False
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "New user created!"})


@app.route("/user/public_id", methods=["PUT"])
def edit_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({"message": "User not found!"})

    user.is_admin = True
    db.session.commit()

    return jsonify({"message": "User has been updated"})


@app.route("/user/public_id", methods=["DELETE"])
def delete_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({"message": "User not found!"})

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User has been deleted"})


if __name__ == "__main__":
    app.run(debug=True)
