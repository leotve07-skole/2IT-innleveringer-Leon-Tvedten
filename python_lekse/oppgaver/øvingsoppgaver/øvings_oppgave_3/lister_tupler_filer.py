#Oppgave 1
planeter = ["Mars", "Jupiter", "Saturn", "Jorden", "Merkur"]

print(planeter[0])

print(planeter[1])

print(planeter[-1])

planeter.append("Neptun")
print(len(planeter))
#Oppgave 2
planeter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter"]

planeter.remove("Venus")

fjern_planet = planeter.pop(2)

print(f"Planeten som ble fjernet var: {fjern_planet}")


#Oppgave 3

expedisjon = []

reiseplan = input("Hvilke 3 planeter vil du besøke?").split()
print("Reiseplain:")
for index, planet in enumerate(reiseplan):
    print(f"{index} {planet}")

#Oppgave 4

indre_planeter = ("Merkur", "Venus", "Jorden", "Mars")

print(indre_planeter)

print(indre_planeter[1])

for i in indre_planeter:
    print(i)

#Å endre en tuple verdi går ikke, det kommer error. Error: TypeError: "tuple" object does not support item assignment
indre_planeter[-1] = "Jupiter"