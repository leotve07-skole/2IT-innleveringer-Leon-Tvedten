import random
import time
from rich import print 

aksje = 0
kurs = []
start_kurs = 100.0

penger = 1000
for x in range(100):
    endring = random.uniform(-5, 5)
    start_kurs += endring
    kurs.append(start_kurs)
    if len(kurs) >= 2:
        kurs_print = f"Kurs: [light_green]↑ {kurs[-1]:.2f}[/light_green] kr" if kurs[-1] > kurs[-2] else f"Kurs: [red]↓ {kurs[-1]:.2f}[/red] kr "
        print(kurs_print)
        time.sleep(5)
    

    
