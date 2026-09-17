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