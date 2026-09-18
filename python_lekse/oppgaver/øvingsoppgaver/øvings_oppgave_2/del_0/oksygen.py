def vurder_oksygen(prosent):
    oksygen_melding = (f"Oksygen: {prosent} %")
    if prosent >= 50:
        return (f"{oksygen_melding}\nOksygennivå OK")
    else:
        return (f"{oksygen_melding}\nLavt oksygennivå")

def les_oksygen():
    fil = open("oksygen.txt", "r")
    oksygen = int(fil.read())
    fil.close()
    return oksygen

oksygen = les_oksygen()
print(vurder_oksygen(oksygen))

