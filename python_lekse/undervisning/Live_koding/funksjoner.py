
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


def romhilsen():
    return "Velkommen til romstasjonen!"\
            "\nGjør deg klar for avreise."

print(romhilsen())
print(romhilsen())
print(romhilsen())

def austronat():
    return "Astronaut: Nora"\
           "\nNora er klar for oppdrag!"\
           "\nAstronaut: Elias"\
           "\nElias er klar for oppdrag!"\
           "\nAstronaut Sara:"\
           "Sara er klar for oppdrag!"
print(austronat)

def vis_maane():
    return "Måne: Europa\
            \nPlanet: Jupiter\
            \nMåne: Titan\
            \nPlanet: Saturn\
            \nMåne: Phobos\
            \nPlanet: Mars"
print(vis_maane())

def beregn_reise(fart, tid):
    avstand = fart * tid
    avstand_tekst = f"Romskipet har reist {avstand} km."
    if avstand < 5000:
        return avstand_tekst + "\nKort reise."
    elif avstand < 20000:
        return avstand_tekst + "\nMellomlang reise."
    else:
        return avstand_tekst + "\nLang reise."

print(beregn_reise(200, 10))