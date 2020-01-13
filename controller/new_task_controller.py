from configuration.config import app
from constants import http_method


@app.route("/task", method=http_method.PUT)
def new_task() -> dict:
    return dict()
