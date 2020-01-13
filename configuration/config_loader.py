import yaml


def load_configuration() -> dict:
    with open("configuration/config.yml", "r") as config:
        return yaml.load(config, yaml.FullLoader)
