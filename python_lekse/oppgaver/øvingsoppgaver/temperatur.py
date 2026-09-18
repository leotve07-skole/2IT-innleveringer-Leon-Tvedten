def les_temperatur():
    fil = open("temperatur.txt", "r")
    temperatur = int(fil.read())
    fil.close()
    return temperatur
def vurder_temperatur(temperatur):
    temp_tekst = f"Temperatur: {temperatur} grader"
    if temperatur < 0:
        return f"{temp_tekst}\n Under frysepunktet"
    else:
        return f"{temp_tekst}\n Over frysepunktet"
temp = les_temperatur()
print(vurder_temperatur(temp))


