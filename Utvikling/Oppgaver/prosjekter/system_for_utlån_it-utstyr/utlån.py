import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
linjer = "-" * 20
print("\n")


class Utstyr :
    def __init__(self):
        self.navn = []
        self.utlant = []
        self.laner = []
        self.utstyr_id = []
        self.lant_id = []

    def registrer_utstyr(self):
        registrert_utstyr = input(f"Skriv utstyr som skal registreres\n")
        clear_console()
        self.utstyr_id.append(1 + self.utstyr_id[-1]) if len(self.utstyr_id) > 0 else self.utstyr_id.append(1)
        self.navn.append(registrert_utstyr)

    def lan_utstyr(self):
        lant_utstyr = input("Skriv self.utstyr_id som skal lanes\n")

        self.utlant.append(lant_utstyr)

        laner_navn = input("Skriv ditt navn\n")

        clear_console()
        self.laner.append(laner_navn)
        
        self.lant_id.append(int(lant_utstyr))
        self.utstyr_id.pop(int(lant_utstyr) - 1) 

    def presenter_utstyr(self):
        if len(self.utstyr_id) < 1:
            if len(self.utlant) > 0: 
                print("Ingen utstyr tilgjengelig, alle er lånt bort.")
            else:
                print("Ingen registrerte utstyr")
        if len(self.utlant) > 0:
            for i in range(len(self.utlant)):
                print(f"\n{linjer}")
                print(f"Utstyr id: {self.lant_id[i]} med navn : {self.navn[i]} er utlånt til {self.laner[i]}")
                print(linjer)
        for i in range(len(self.utstyr_id)):
            print(f"\n{linjer}")
            print(f"{self.utstyr_id[i]} : {self.navn[i]}")
            print(linjer)


utstyr = Utstyr()
while True:
    print(f"\n{linjer}\nValg:\n{linjer}\n1. registrer_utstyr\n{linjer}\n2. lan_utstyr\n{linjer}")
    utstyr.presenter_utstyr()

    print("\n\n")
    bruker_valg = input()
    print(f"{linjer}\n")
    if bruker_valg == "1":
        utstyr.registrer_utstyr()
    if bruker_valg == "2":
        utstyr.lan_utstyr()


