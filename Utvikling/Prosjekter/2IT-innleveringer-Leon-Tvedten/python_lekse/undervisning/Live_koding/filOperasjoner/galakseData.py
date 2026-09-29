try:
    with open("filOperasjoner/galakse.txt", "r") as fil:
        print(fil.read)
except FileNotFoundError:
    print("Filen finnes ikke")

try:
    planetNummer = int(input("Velg planetnummer "))
except ValueError:
    print("Du må skrive inn ett gyldig tall")
else:
    print(planetNummer)