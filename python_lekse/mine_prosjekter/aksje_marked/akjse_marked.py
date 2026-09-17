import random
import time
import json
import curses
from data import db

aksjer = db["aksjer"]
konto = db["konto"]
penger = konto["penger"]

def aksje_spill(stdscr):
    global penger
    stdscr.nodelay(True)
    curses.start_color()
    max_y, max_x = stdscr.getmaxyx()
    graf_x = 0
    graf_y = max_y // 2
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    c_green = curses.color_pair(1)
    c_red = curses.color_pair(2)
    sist_oppdatert = time.time()
    aksje_farger = [curses.color_pair(3), curses.color_pair(4), curses.color_pair(5)]

    def vis_kurs(aksje, y, x):
        if len(aksje["kurs"]) >= 2:
            kurs = aksje["kurs"][-1]
            forrige_kurs = aksje["kurs"][-2]
            stdscr.move(y, x)
            stdscr.clrtoeol()
            stdscr.addstr(y, x, " : ")
            if kurs > forrige_kurs:
                tekst = f"↑ {kurs:.2f} kr"
                stdscr.addstr(y, x + 3, tekst, c_green)
            else:
                tekst = f"↓ {kurs:.2f} kr"
                stdscr.addstr(y, x + 3, tekst, c_red)
            return len(tekst) if len(tekst) > 0 else 0
        return 0
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
    while True:
        kommando = stdscr.getch()
        modus = quit_kommando(kommando, modus)
        time.sleep(0.2)
        navn = list(aksjer.keys())
        if modus == "kurs":
            for i, aksje_navn in enumerate(navn):
                valg = kommando - ord("1")
                aksje = aksjer[aksje_navn]
                x = 0
                if aksje["aksje_beholdning"] > 0 and aksje["kjøps_verdi_beholdning"] > 0:
                    markedsverdi = aksje["aksje_beholdning"] * aksje["kurs"][-1]
                    avkastning = markedsverdi - aksje["kjøps_verdi_beholdning"]
                    avkastning_i_prosent = (avkastning / aksje["kjøps_verdi_beholdning"]) * 100
                else:
                    avkastning = 0.0
                    avkastning_i_prosent = 0.0
                vis_kurs_lengde = f"↑ {max(aksje["kurs"]):.2f} kr"
                kurs_tekst = f"{i + 1}: {aksje_navn} : {vis_kurs_lengde} Avkastning: {avkastning:.2f} kr .{avkastning_i_prosent:.2f}%"
                content_width = len(kurs_tekst)
                place_kurs_middle = (max_x - content_width) // 2
                differanse_farge = c_green if avkastning > 0 else c_red
                stdscr.addstr(i + 1, place_kurs_middle + x + 3, f" Avkastning: {avkastning:.2f} kr {"+" if avkastning > 0 else ""}{avkastning_i_prosent:.2f}%".ljust(50), differanse_farge)
                
                for l in range(len(aksje["kurs"])) :
                    aksje["kurs"][l] = max(0, int(aksje["kurs"][l]))
                if modus == "kurs":
                    stdscr.addstr(i + 1, place_kurs_middle + 1, f"{i + 1}: {aksje_navn}", aksje_farger[i])
                    x = len(f"{i + 1}: {aksje_navn}") + 1
                    x += vis_kurs(aksje, i + 1, place_kurs_middle + x)
            for column in range(place_kurs_middle, place_kurs_middle + len(kurs_tekst) + 5):
                stdscr.addstr(len(navn) + 1 + max_y // 2, column, "-")
                stdscr.addstr(max_y // 2, column, "-")
            for row in range(len(navn)):
                row += 1
                stdscr.addstr(row + max_y // 2, place_kurs_middle, "╎")
                stdscr.addstr(row + max_y // 2, column, "╎")
            if time.time() - sist_oppdatert >= 1:
                for aksje_navn in navn:
                    aksje = aksjer[aksje_navn]

                    endring = random.uniform(-5, 5)
                    aksje["start_kurs"] += endring
                    aksje["kurs"].append(aksje["start_kurs"])
                if modus == "graf":
                    if aksje["kurs"][-1] > aksje["kurs"][-2]:
                        graf_y -= 1
                        stdscr.addch(graf_y, graf_x, "*", c_green)
                    else:
                        graf_y += 1
                        stdscr.addch(graf_y, graf_x, "*", c_red)
                    graf_x += 1
                    graf_y = max(0, min(graf_y, max_y - 1))

                sist_oppdatert = time.time()
            stdscr.refresh()
            if 0 <= valg < len(navn):
                stdscr.clear()
                valgt_aksje = aksjer[navn[valg]]
                modus = "valgt_aksje"
        elif modus == "valgt_aksje":
                stdscr.clear()
                stdscr.move(i, len(navn[valg]))
                stdscr.clrtoeol()
                stdscr.addstr(i, 0, f"{navn[valg]}", aksje_farger[valg])
                vis_kurs(valgt_aksje, i, len(navn[valg]))

                stdscr.addstr(4, 0, "b = kjøp")
                stdscr.addstr(5, 0, "s = selg")
                stdscr.addstr(6, 0, "g = graf")
                        
                stdscr.refresh()
                if kommando == ord("b"):
                    modus = "kjøp_aksje"
                    stdscr.clear()
                    stdscr.refresh()
                    stdscr.addstr(2, 0, f"{navn[valg]}", aksje_farger[valg])
                    vis_kurs(valgt_aksje, 2,len(navn[valg]))
                    stdscr.addstr(4, 0, f"Hvor mange ")
                    stdscr.addstr(4, len("Hvor mange "), f"{navn[valg]}", aksje_farger[valg])
                    stdscr.addstr(" aksjer vil du kjøpe?")
                    stdscr.addstr(6, 0, "du har ")
                    stdscr.addstr(f"{penger:.2f} kr ", c_green)
                    stdscr.addstr("på kontoen")
                    stdscr.refresh()
                    kjøp_aksjer = hent_tall(stdscr, 4, 35)
                    pris_for_kjøp = kjøp_aksjer * valgt_aksje["kurs"][-1]
                    valgt_aksje["total_penger_brukt"] += pris_for_kjøp
                    stdscr.clear()
                    if (penger - pris_for_kjøp) >= 0:
                        valgt_aksje["aksje_beholdning"] += kjøp_aksjer
                        penger -= pris_for_kjøp
                        valgt_aksje["kjøps_verdi_beholdning"] += pris_for_kjøp
                        stdscr.addstr(4, 0, f"Du har kjøpt ")
                        stdscr.addstr(f"{kjøp_aksjer} ", c_green)
                        stdscr.addstr("aksjer for ")
                        stdscr.addstr(f"{pris_for_kjøp:.2f} kr", c_red)
                        stdscr.addstr(6, 0, "Din aksje beholdning er nå verdt ")
                        stdscr.addstr(f"{(valgt_aksje["aksje_beholdning"] * valgt_aksje["kurs"][-1]):.2f}", c_green)
                        stdscr.addstr(8, 0, "Du har ")
                        stdscr.addstr(f"{penger:.2f} kr ", c_red) 
                        stdscr.addstr("igjen på kontoen.")
                        stdscr.addstr(10, 0, "Du har nå ")
                        stdscr.addstr(f"{valgt_aksje["aksje_beholdning"]} ")
                        stdscr.addstr(10, len(f"Du har nå {valgt_aksje["aksje_beholdning"]}"), f"{navn[valg]} ", aksje_farger[valg])
                        stdscr.addstr("aksjer")
                        stdscr.refresh()
                        time.sleep(6)
                        stdscr.clear()
                        modus = "kurs"
                        with open("data.json", "w") as fil:
                            json.dump(db, fil, indent=4)
                    else:
                        stdscr.addstr(4, 0, "Du har ikke penger nok på konto til å kjøpe ")
                        stdscr.addstr(f"{kjøp_aksjer}", c_red)
                        stdscr.addstr("aksjer")
                        time.sleep(3)
                        stdscr.clear()
                        modus = "kurs"
                elif kommando == ord("s"):
                    modus = "selge_aksje"
                    stdscr.clear()
                    stdscr.addstr(1, 0, f"{navn[valg]}", aksje_farger[valg])
                    vis_kurs(aksje, 1, (len(navn[valg])))
                    stdscr.addstr(3, 0, temp_text := f"Du har {valgt_aksje["aksje_beholdning"]} ")
                    stdscr.addstr(3, len(temp_text), navn[valg], aksje_farger[valg])
                    stdscr.addstr(" aksjer")
                    stdscr.addstr(4, 0, temp_text := "Aksjeverdien tilsvarer ")
                    stdscr.addstr(4, len(temp_text), f"{(valgt_aksje["aksje_beholdning"] * valgt_aksje["kurs"][-1]):.2f}", c_green)
                    stdscr.addstr(5, 0, "Hvor mange aksjer av hvilken vil du selge?")
                    del temp_text
                    stdscr.refresh()
                    selg_aksjer = hent_tall(stdscr, 4, 35)
                    stdscr.clear()
                    if (valgt_aksje["aksje_beholdning"] - selg_aksjer) >= 0:
                        snittpris = valgt_aksje["kjøps_verdi_beholdning"] / valgt_aksje["aksje_beholdning"] if valgt_aksje["aksje_beholdning"] > 0 else 0
                        valgt_aksje["aksje_beholdning"] -= selg_aksjer
                        penger += (selg_aksjer * aksje["kurs"][-1])
                        valgt_aksje["kjøps_verdi_beholdning"] -= (selg_aksjer * snittpris)
                        stdscr.addstr(4, 0, temp_text := "Du solgte ")
                        stdscr.addstr(f"{selg_aksjer} ", c_green)
                        temp_text += f"{selg_aksjer} "
                        stdscr.addstr(4, len(temp_text), navn[valg], aksje_farger[valg])
                        stdscr.addstr(" aksjer for ")
                        stdscr.addstr(f"{(selg_aksjer * valgt_aksje["kurs"][-1]):.2f} kr", c_green)
                        stdscr.addstr(6, 0, "Du har nå ")
                        stdscr.addstr(f"{penger:.2f} kr ", c_green)
                        stdscr.addstr("på kontoen")
                        stdscr.refresh()
                        time.sleep(6)
                        stdscr.clear()
                        modus = "kurs"
                        with open("data.json", "w") as fil:
                            json.dump(db, fil, indent=4)

                    else:
                        stdscr.clear()
                        stdscr.addstr(4, 0, f"Du har ikke nok antall aksjer til å selge {selg_aksjer} aksjer")
                        stdscr.refresh()
                        time.sleep(3)
                        stdscr.clear()
                        modus = "kurs"
                elif kommando == ord("g"):
                    stdscr.clear()
                    stdscr.refresh()
                    modus = "graf"
                    stdscr.refresh()
            
        stdscr.refresh()
with open("data.json", "w") as fil:
    json.dump(db, fil, indent=4)    
if __name__ == "__main__":
    curses.wrapper(aksje_spill)