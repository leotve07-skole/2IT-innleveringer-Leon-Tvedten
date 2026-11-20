import os
from collections import defaultdict

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
linjer = "-" * 20
print("\n")


class Utstyr :
    def __init__(self):
        self.utstyr = defaultdict(dict)
        self.lant_utstyr = defaultdict(dict)
        self.id = 1

    def registrer_utstyr(self):
        registrert_utstyr = input(f"Skriv utstyr som skal registreres\n")
        clear_console()
        self.utstyr["id"][self.id] = registrert_utstyr
 
        self.id += 1
    def lanet_utstyr(self):
        lant_utstyr = int(input("Skriv utstyr id som skal lånes\n"))

        laner_navn = input("Skriv ditt navn\n")
        if lant_utstyr in self.utstyr["id"]:
            self.lant_utstyr["id"][lant_utstyr] = [laner_navn, self.utstyr["id"][lant_utstyr]]

        clear_console()

        del self.utstyr["id"][lant_utstyr]

    def presenter_utstyr(self):
        if not self.utstyr["id"]:
            if self.lant_utstyr["id"]: 
                print("Ingen utstyr tilgjengelig, alle er lånt bort.")
            else:
                print("Ingen registrerte utstyr")
        if self.lant_utstyr["id"]:
           for k in self.lant_utstyr["id"].keys():
            print("\nLånt utstyr:")
            print(f"{k} : {self.lant_utstyr["id"][k]}")
        
        for n in self.utstyr["id"].keys():
            print(f"\n{linjer}")
            print(f"{n} : {self.utstyr["id"][n]}")
            print(linjer)


utstyr = Utstyr()
while True:
    clear_console()
    print(f"\n{linjer}\nValg:\n{linjer}\n1. registrer_utstyr\n{linjer}\n2. lan_utstyr\n{linjer}")
    utstyr.presenter_utstyr()

    print("\n\n")
    bruker_valg = input()
    print(f"{linjer}\n")
    if bruker_valg == "1":
        utstyr.registrer_utstyr()
    if bruker_valg == "2":
        utstyr.lanet_utstyr()


