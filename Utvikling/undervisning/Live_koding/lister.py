solsystem = ["Venus", "Merkur", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]

nyPlanet = "Pluto"
solsystem.append(nyPlanet)

solsystem.insert(1, "Aries")
print(solsystem)
solsystem.pop(1)
print(solsystem)

for planet in solsystem:
    if planet == "Venus":
        print(planet, "Eksisterer")

tall = (12, 45, 40)

for tallVerdi in tall:
    print(tallVerdi * 2)

for index, planet in enumerate(solsystem):
    print(index, planet)