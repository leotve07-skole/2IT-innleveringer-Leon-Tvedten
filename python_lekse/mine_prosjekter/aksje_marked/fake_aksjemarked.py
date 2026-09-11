import random
import time
import json
import threading
import queue
from rich import print 
from data import db

kommandoer = queue.Queue()

def input_loop():
    while True:
        kommando = input()
        kommandoer.put(kommando.lower())
      
threading.Thread(target=input_loop, daemon=True).start()

for x in range(100):     
    endring = random.uniform(-5, 5)
    db["start_kurs"] += endring
    db["kurs"].append(db["start_kurs"])
    if len(db["kurs"]) >= 2:
        kurs_print = f"Kurs: [light_green]↑ {db["kurs"][-1]:.2f}[/light_green] kr" if db["kurs"][-1] > db["kurs"][-2] else f"Kurs: [red]↓ {db["kurs"][-1]:.2f}[/red] kr "
        print(kurs_print)
        time.sleep(1)
        print("Hvis du vil kjøpe aksjer skriv <b>")
        if not kommandoer.empty():
            kommando = kommandoer.get()
            if kommando == "b":
                print(f"Hvor mange aksjer vil du kjøpe?\n{kurs_print}\
                    \ndu har [light_green]{db["penger"]}[/light_green] kr på kontoen")
                kjøp_aksjer = int(kommandoer.get())
                if (db["penger"] - (kjøp_aksjer * db["kurs"][-1])) >= 0:
                    db["aksje_beholdning"] += kjøp_aksjer
                    db["penger"] -= (kjøp_aksjer * db["kurs"][-1])
                    db["aksje_beholdning"] = kjøp_aksjer
                    print(f"Du har kjøpt [light_green]{kjøp_aksjer}[/light_green] aksjer for [red]{(kjøp_aksjer * db["kurs"][-1]):.2f}[/red] kr. \
                    \nDin aksje beholdning er nå verdt [light_green]{db["aksje_beholdning"]:.2f}[/light_green] \
                    \nDu har [red]{db["penger"]:.2f}[/red] kr igjen på kontoen")
                    with open("data.json", "w") as fil:
                        json.dump(db, fil)
                else:
                    print(f"Du har ikke penger nok på konto til å kjøpe [red]{kjøp_aksjer}[/red] aksjer")
            

        

        
