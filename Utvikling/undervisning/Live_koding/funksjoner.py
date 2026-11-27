
def vis_planet(planet, antall_maaner):
    print("--------------------")
    print(f"Velkommen til " + planet)
    print("--------------------")
    print("Antall måner: ", antall_maaner)
vis_planet("Mars", 8)

def beregn_avstand(fart, timer):
    avstand = fart * timer
    return avstand
resultat = beregn_avstand(43223, 3232)
print(resultat)

def vurder_temperatur(temperatur):
    if temperatur < -100:
        return "Ekstremt kaldt"
    elif temperatur < 0:
        return "Kaldt"
    elif temperatur < 30:
        return "Varmt og godt"
    else:
        return "Veldig varmt"

print(vurder_temperatur(24))

#En funksjon som regner ut hvor mye drivstoff et romskip bruker
def drivstoff_forbruk_romskip(tid, forbruk_per_time):
    return tid * forbruk_per_time
print(drivstoff_forbruk_romskip(1000, 1090))
