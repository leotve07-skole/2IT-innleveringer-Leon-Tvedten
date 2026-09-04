navn = "Ola"


alder = 18
hoyde = 1.75
liker_python = True

print(navn)
print(alder)
print(hoyde)
print(liker_python)

print(type(navn))
print(type(alder))
print(type(hoyde))
print(type(liker_python))

pris = 30
antall = 4

total = pris * antall
print(total)

if alder >= 18:
    print("Du er myndig")
else:
    print("Du er ikke myndig")


if alder < 13:
    print("barn")
elif alder < 18:
    print("Ungdom")
else:
    print("Voksen")

    