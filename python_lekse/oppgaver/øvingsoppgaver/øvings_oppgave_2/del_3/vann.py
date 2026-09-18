def les_vann():
    fil = open("vann.txt", "r")
    vann = int(fil.read())
    fil.close()
    return vann

def vurder_vann(liter):
    vann_tekst = f"Vann igjen: {liter} liter"

    if liter <= 25:
        return f"{vann_tekst}\n Nok vann"
    else:
        return f"{vann_tekst}\n Lite vann"

a_vann = les_vann()
print(vurder_vann(a_vann))
