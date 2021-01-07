from flask import Flask, jsonify
from flask import request
import logging


def create_app():

    app = Flask(__name__)

    @app.route("/")
    def index():
        return "hello world"

    @app.route("/log_response_text/")
    def log_response_text():
        response_text = "hello world logged"
        app.logger.info(response_text)
        app.logger.info("__name__ is {}".format(__name__))
        return response_text

    @app.route("/log_response_json/")
    def log_response_json():
        response_dict = {"foo": ["bar1", "bar2"], "foofoo": "bar3"}
        app.logger.info(response_dict)
        return jsonify(response_dict)

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=8000, debug=True)

elif __name__ != "__main__":
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app = create_app()
    app.logger.handlers = gunicorn_logger.handlers #change the app object's logger to the Gunicorn handler
    app.logger.setLevel(gunicorn_logger.level) #set the level of app object's logger to that of the Gunicorn handler