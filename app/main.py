from flask import Flask

from configuration import config
from configuration.config_loader import load_configuration
from app.constants import config_keys


def _main():
    deploy_conf: dict = load_configuration().get(config_keys.DEPLOY)
    config.app = Flask(__name__)
    config.app.run(
        host=deploy_conf[config_keys.HOST],
        port=deploy_conf[config_keys.PORT],
        debug=deploy_conf[config_keys.DEBUG]
    )


if __name__ == '__main__':
    _main()
