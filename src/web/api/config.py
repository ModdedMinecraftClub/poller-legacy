import yaml


def get_config():
    stream = open("db_config.yml", "r")

    return yaml.safe_load(stream)
