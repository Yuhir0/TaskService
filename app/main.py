from flask import Flask, Config
from flask_injector import FlaskInjector
from injector import inject
from app.configuration import config
from app.configuration.config_loader import load_configuration
from app.constants import config_keys


def _main():
    deploy_conf: dict = load_configuration().get(config_keys.DEPLOY)
    app = Flask(__name__)
    app.config.update()
    config.app.run(
        host=deploy_conf[config_keys.HOST],
        port=deploy_conf[config_keys.PORT],
        debug=deploy_conf[config_keys.DEBUG]
    )

    FlaskInjector(app=app)


if __name__ == '__main__':
    _main()
