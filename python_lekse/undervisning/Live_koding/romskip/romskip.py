def vurder_drivstoff():
    if drivstoff >= 50:
        print("Nok drivstoff")
    else:
        print("For lite drivstoff")

def les_drivstoff(drivstoff):
    fil = open("drivstoff.txt", "r")
    drivstoff = int(fil.read())
    fil.close()
    return drivstoff
drivstoff = les_drivstoff(50)
print(drivstoff)
print(f"Drivstoff: {drivstoff} %")

