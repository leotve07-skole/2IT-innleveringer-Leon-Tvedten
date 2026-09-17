import os
import json

db = {
    "stats":{
        "money": 0
    }
}
if os.path.exists("data.json"):
    with open(os.path.join(os.path.dirname(__file__), "data.json"), "r") as fil:
        db = json.load(fil)
