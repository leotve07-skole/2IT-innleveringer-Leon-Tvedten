import os
import json

db = {
"aksje_beholdning" : 0,
"aksje_beholdning_verdi" : 0,
"kurs" : [],
"start_kurs" : 100.0,
"penger" : 1000,
"kjøps_verdi_beholdning": 0,
"total_penger_brukt" : 0
}

if os.path.exists("data.json"):
    with open("data.json", "r") as fil:
        db = json.load(fil)
