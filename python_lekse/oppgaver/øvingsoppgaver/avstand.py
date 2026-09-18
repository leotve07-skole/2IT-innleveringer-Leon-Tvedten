def les_avstand():
    fil = open("avstand.txt", "r")
    avstand = int(fil.read())
    fil.close()
    return avstand

def vurder_avstand(avstand):
    avstand_tekst = f"Avstand: {avstand} km"

    if avstand < 10000:
        return f"{avstand_tekst}\n Narme"
    else:
        return f"{avstand_tekst}\n Langt unna"

avs = les_avstand()
print(vurder_avstand(avs))
