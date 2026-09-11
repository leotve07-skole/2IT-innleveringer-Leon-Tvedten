import random
import time
from rich import print 

aksje = 0
kurs = []
start_kurs = 100.0

for x in range(100):
    endring = random.uniform(-5, 5)
    start_kurs += endring
    kurs.append(start_kurs)
    if len(kurs) >= 2:
        if kurs[-1] > kurs[-2]:
          print(f"Kurs: [light_green]{kurs[-1]:.2f}[/light_green] kr")
        else: 
            print(f"Kurs: [red]{kurs[-1]:.2f}[/red] kr")
       
        time.sleep(1)



