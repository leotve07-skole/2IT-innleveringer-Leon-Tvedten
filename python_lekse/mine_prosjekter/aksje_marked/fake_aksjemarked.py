import random
import time
from rich import print 

db = {
"aksje_beholdning" : 0,
"aksje_beholdning_verdi" : 0,
"kurs" : [],
"start_kurs" : 100.0,
"penger" : 1000
}
for x in range(100):     
    endring = random.uniform(-5, 5)
    db["start_kurs"] += endring
    db["kurs"].append(db["start_kurs"])
    if len(db["kurs"]) >= 2:
        kurs_print = f"Kurs: [light_green]↑ {db["kurs"][-1]:.2f}[/light_green] kr" if db["kurs"][-1] > db["kurs"][-2] else f"Kurs: [red]↓ {db["kurs"][-1]:.2f}[/red] kr "
        print(kurs_print)
        time.sleep(1)
        svar = input("Hvis du vil kjøpe aksjer skriv <kjøp aksjer>")

        if svar == "kjøp aksjer":
            print(f"Hvor mange aksjer vil du kjøpe?\n{kurs_print}")
            kjøp_aksjer = int(input())
            db["aksje_beholdning"] += kjøp_aksjer
            db["penger"] -= (kjøp_aksjer * db["kurs"][-1])
            db["aksje_beholdning"] = (db["aksje_beholdning"] * db["kurs"][-1])
            print(f"Du har kjøpt [light_green]{kjøp_aksjer}[/light_green] aksjer for [red]{(kjøp_aksjer * db["kurs"][-1]):.2f}[/red] kr. \
               \nDin aksje beholdning er nå verdt [light_green]{db["aksje_beholdning"]:.2f}[/light_green] \
               \nDu har [red]{db["penger"]:.2f}[/red] kr igjen på kontoen")
        
        

    
    

    
