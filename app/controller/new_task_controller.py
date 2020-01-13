from flask import Flask
from flask_injector import FlaskInjector
from injector import inject

from app.constants import http_method


@inject
def flask_app() -> Flask:
    return app


@app.route("task", methods=[http_method.PUT])
def new_task() -> dict:
    return dict()
