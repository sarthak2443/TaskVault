from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return jsonify({"msg": "TaskVault API working!"})
