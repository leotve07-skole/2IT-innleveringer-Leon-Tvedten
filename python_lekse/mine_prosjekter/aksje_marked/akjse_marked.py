import random
import time
import json
import curses
from data import db

def aksje_spill(stdscr):
    stdscr.nodelay(True)
    curses.start_color()
    max_y, max_x = stdscr.getmaxyx()
    graf_x = 0
    graf_y = max_y // 2
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    c_green = curses.color_pair(1)
    c_red = curses.color_pair(2)
    sist_oppdatert = time.time()

    def vis_kurs(y, x):
        kurs = db["kurs"][-1]
        forrige_kurs = db["kurs"][-2]
        stdscr.addstr(y,x, "Kurs: ")
        if kurs > forrige_kurs:
            stdscr.addstr(y, x + 6, f"↑ {db["kurs"][-1]:.2f} kr", c_green)
        else:
            stdscr.addstr(y, x + 6, f"↓ {db["kurs"][-1]:.2f} kr", c_red)
        stdscr.refresh()
    def hent_tall(stdscr, y, x):
        stdscr.nodelay(False)
        tall = int(stdscr.getstr(y, x).decode())
        stdscr.nodelay(True)
        return tall
    def quit_kommando(kommando, modus):
        if kommando == ord("q"):
            stdscr.clear()
            modus = "kurs"
        return modus
    modus = "kurs"
    for x in range(1000):
        time.sleep(0.1)
        if time.time() - sist_oppdatert >= 1:
            endring = random.uniform(-5, 5)
            db["start_kurs"] += endring
            db["kurs"].append(db["start_kurs"])
            if modus == "graf":
                if db["kurs"][-1] > db["kurs"][-2]:
                    graf_y -= 1
                    stdscr.addch(graf_y, graf_x, "*", c_green)
                else:
                    graf_y += 1
                    stdscr.addch(graf_y, graf_x, "*", c_red)
                graf_x += 1
                graf_y = max(0, min(graf_y, max_y - 1))

            sist_oppdatert = time.time()
        stdscr.refresh()
        time.sleep(0.05)
        kommando = stdscr.getch()
        modus = quit_kommando(kommando, modus)
        if modus == "kurs":     
            if len(db["kurs"]) >= 2:
                stdscr.addstr(4, 0,
                    "Hvis du vil kjøpe aksjer skriv <b>\n"
                    "Hvis du vil selge aksjer skriv <s>\n"
                    "Skriv <g> hvis du vil se grafisk aksje kursen"
                    )
                vis_kurs(8, 0)
            if kommando == ord("b"):
                stdscr.clear()
                stdscr.refresh()
                stdscr.addstr(4, 2, f"Hvor mange aksjer vil du kjøpe?")
                vis_kurs(2,2)
                stdscr.addstr(6, 2, "du har ")
                stdscr.addstr(f"{db["penger"]:.2f} ", c_green)
                stdscr.addstr("kr på kontoen")
                stdscr.refresh()
                kjøp_aksjer = hent_tall(stdscr, 4, 35)
                pris_for_kjøp = kjøp_aksjer * db["kurs"][-1]
                db["total_penger_brukt"] += pris_for_kjøp
                stdscr.clear()
                if (db["penger"] - pris_for_kjøp) >= 0:
                    db["aksje_beholdning"] += kjøp_aksjer
                    db["penger"] -= pris_for_kjøp
                    db["kjøps_verdi_beholdning"] += pris_for_kjøp
                    stdscr.addstr(4, 2, f"Du har kjøpt ")
                    stdscr.addstr(f"{kjøp_aksjer} ", c_green)
                    stdscr.addstr("aksjer for ")
                    stdscr.addstr(f"{pris_for_kjøp:.2f} kr", c_red)
                    stdscr.addstr(6, 2, "Din aksje beholdning er nå verdt ")
                    stdscr.addstr(f"{(db["aksje_beholdning"] * db["kurs"][-1]):.2f}", c_green)
                    stdscr.addstr(8, 2, "Du har ")
                    stdscr.addstr(f"{db["penger"]:.2f} ", c_red) 
                    stdscr.addstr("kr igjen på kontoen.")
                    stdscr.addstr(10, 2, "Du har nå ")
                    stdscr.addstr(f"{db["aksje_beholdning"]} aksjer")
                    stdscr.refresh()
                    time.sleep(8)
                    stdscr.clear()
                    with open("data.json", "w") as fil:
                        json.dump(db, fil)
                else:
                    stdscr.addstr(4, 2, "Du har ikke penger nok på konto til å kjøpe ")
                    stdscr.addstr(f"{kjøp_aksjer}", c_red)
                    stdscr.addstr("aksjer")
            elif kommando == ord("s"):
                stdscr.clear()
                stdscr.refresh()
                stdscr.addstr(4, 2, f"Du har {db["aksje_beholdning"]} aksjer")
                stdscr.addstr(6, 2, "Aksjeverdien tilsvarer ")
                stdscr.addstr(f"{(db["aksje_beholdning"] * db["kurs"][-1]):.2f}", c_green)
                stdscr.addstr(8, 2, "Hvor mange aksjer vil du selge?")
                vis_kurs(10, 2)
                selg_aksjer = hent_tall(stdscr, 4, 35)
                stdscr.clear()
                if (db["aksje_beholdning"] - selg_aksjer) >= 0:
                    snittpris = db["kjøps_verdi_beholdning"] / db["aksje_beholdning"] if db["aksje_beholdning"] > 0 else 0
                    db["aksje_beholdning"] -= selg_aksjer
                    db["penger"] += (selg_aksjer * db["kurs"][-1])
                    db["kjøps_verdi_beholdning"] -= (selg_aksjer * snittpris)
                    stdscr.addstr(4, 2,"Du solgte ")
                    stdscr.addstr(f"{selg_aksjer} ", c_green)
                    stdscr.addstr("aksjer for ")
                    stdscr.addstr(f"{(selg_aksjer * db["kurs"][-1]):.2f} kr", c_green)
                    stdscr.addstr(6, 2, "Du har nå ")
                    stdscr.addstr(f"{db["penger"]:.2f} kr ", c_green)
                    stdscr.addstr("på kontoen")
                    stdscr.refresh()
                    time.sleep(8)
                    stdscr.clear()
                    with open("data.json", "w") as fil:
                        json.dump(db, fil)
                else:
                    stdscr.addstr(4, 2, f"Du har ikke nok antall aksjer til å selge {selg_aksjer} aksjer")
            elif kommando == ord("g"):
                stdscr.clear()
                stdscr.refresh()
                modus = "graf"
            if db["aksje_beholdning"] > 0:
                markedsverdi = db["aksje_beholdning"] * db["kurs"][-1]
                avkastning = markedsverdi - db["kjøps_verdi_beholdning"]
                avkastning_i_prosent = (avkastning / db["kjøps_verdi_beholdning"]) * 100
            else:
                avkastning = 0.0
            differanse_farge = c_green if avkastning > 0 else c_red
            stdscr.addstr(9, 0, f"Avkastning: {avkastning:.2f} kr {"+" if avkastning > 0 else ""}{avkastning_i_prosent:.2f}%".ljust(50), differanse_farge)
            stdscr.refresh()
        
        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(aksje_spill)