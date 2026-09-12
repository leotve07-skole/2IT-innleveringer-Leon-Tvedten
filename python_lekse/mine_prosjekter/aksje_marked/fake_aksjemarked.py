import random
import time
import json
import threading
import queue
import curses
from rich import print as rprint
from data import db

def aksje_spill(stdscr):
    stdscr.nodelay(True)
    max_y, max_x = stdscr.getmaxyx()
    graf_x = 0
    graf_y = max_y // 2
    kommandoer = queue.Queue()

    def input_loop():
        while True:
            kommando = stdscr.getch()
            kommandoer.put(kommando)
        
    threading.Thread(target=input_loop, daemon=True).start()

    modus = "kurs"
    for x in range(1000):
        endring = random.uniform(-5, 5)
        db["start_kurs"] += endring
        db["kurs"].append(db["start_kurs"])
        if modus == "kurs":     
            if len(db["kurs"]) >= 2:
                kurs_print = f"Kurs: [light_green]↑ {db["kurs"][-1]:.2f}[/light_green] kr" if db["kurs"][-1] > db["kurs"][-2] else f"Kurs: [red]↓ {db["kurs"][-1]:.2f}[/red] kr "
                stdscr.addstr(2,2, kurs_print)
                time.sleep(1)
                print(
                    "Hvis du vil kjøpe aksjer skriv <b>\n"
                    "Hvis du vil selge aksjer skriv <s>\n"
                    "Skriv <g> hvis du vil se grafisk aksje kursen"
                    )
        kommando = None
        if not kommandoer.empty():
            kommando = kommandoer.get()
            if kommando == ord("b"):
                rprint(f"Hvor mange aksjer vil du kjøpe?\n{kurs_print}\
                    \ndu har [light_green]{db["penger"]:.2f}[/light_green] kr på kontoen")
                kjøp_aksjer = int(kommandoer.get())
                if (db["penger"] - (kjøp_aksjer * db["kurs"][-1])) >= 0:
                    db["aksje_beholdning"] += kjøp_aksjer
                    db["penger"] -= (kjøp_aksjer * db["kurs"][-1])
                    rprint(f"Du har kjøpt [light_green]{kjøp_aksjer}[/light_green] aksjer for [red]{(kjøp_aksjer * db["kurs"][-1]):.2f}[/red] kr. \
                    \nDin aksje beholdning er nå verdt [light_green]{(db["aksje_beholdning"] * db["kurs"][-1]):.2f}[/light_green] \
                    \nDu har [red]{db["penger"]:.2f}[/red] kr igjen på kontoen.\
                    \nDu har nå {db["aksje_beholdning"]} aksjer"
                    )
                    with open("data.json", "w") as fil:
                        json.dump(db, fil)
                else:
                    rprint(f"Du har ikke penger nok på konto til å kjøpe [red]{kjøp_aksjer}[/red] aksjer")
            if kommando == ord("s"):
                rprint(
                    f"Du har {db["aksje_beholdning"]} aksjer.\n"
                    f"Aksjeverdien tilsvarer [light_green]{(db["aksje_beholdning"] * db["kurs"][-1]):.2f}"
                    )
                print("Hvor mange aksjer vil du selge?")
                selg_aksjer = int(kommandoer.get())
                if (db["aksje_beholdning"] - selg_aksjer) >= 0:
                    db["aksje_beholdning"] -= selg_aksjer
                    db["penger"] += (selg_aksjer * db["kurs"][-1])
                    rprint(
                        f"Du solgte [light_green]{selg_aksjer}[/light_green] aksjer for [light_green]{(selg_aksjer * db["kurs"][-1]):.2f}[/light_green] kr\n"
                        f"Du har nå [light_green]{db["penger"]:.2f}[/light_green] kr på kontoen"
                        )
                    with open("data.json", "w") as fil:
                        json.dump(db, fil)
                else:
                    print(f"Du har ikke nok antall aksjer til å selge {selg_aksjer} aksjer")
        if kommando == ord("g"):
            modus = "graf"
        if modus == "graf":
            stdscr.addch(graf_y, graf_x, "*")
            graf_x += 1
            if db["kurs"][-1] > db["kurs"][-2]:
               graf_y -= 1
            else:
                graf_y += 1
        
        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(aksje_spill)