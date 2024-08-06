#!/usr/bin/python3
""" Basic Flask app """

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import environ

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(self):
    """ Closes current SQLAlchemy session """


@app.errorhandler(404)
def not_found(error):
    """ Handle 404 Error """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", 5000)
    app.run(host=host, port=port, threaded=True)
