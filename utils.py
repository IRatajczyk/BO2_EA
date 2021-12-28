import json


def load_config(config_path: str = "config.json") -> dict:
    with open(config_path) as file:
        data = json.load(file)
    return data
