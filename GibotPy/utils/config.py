import json
from os import path, listdir

DATA = path.join("Data")
CONFIG = path.join(DATA, "config.json")

print(listdir(DATA))

def get_config(key: str):
    with open(CONFIG) as f:
        return json.load(f)[key]
