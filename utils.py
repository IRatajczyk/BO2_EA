import json


def load_config(config_path: str = "data/config.json") -> dict:
    with open(config_path) as file:
        data = json.load(file)
    return data


def proceed_test():
    return 1
