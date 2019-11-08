import json
from pathlib import Path
import os


# get_json_data will fetch data from data.json
def get_json_data(key):
    path = Path(__file__).parent.parent
    path = os.path.join(path, "locators")
    os.chdir(path)
    with open('data.json', 'r') as fp:
        data = json.load(fp)
    return data[key]










