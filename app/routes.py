from flask import Blueprint

routes = Blueprint('routes', __name__)

@routes.route("/", methods=["GET"])
def home():
    return {"status" : "started"}

@routes.route("/route", methods=["GET"])
def route():
    return {"status" : "running"}