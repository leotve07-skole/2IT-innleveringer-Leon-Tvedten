try:
    poeng = int(input("Poeng:\n"))

    if poeng <= 49:
        print("Ikke bestått")
    elif poeng <= 69:
        print("Bestått")
    elif poeng <= 89:
        print("Godt")
    elif poeng <= 100:
        print("Meget godt")
    else:
        print("Ugyldig poeng")
except ValueError:
    print("Ugyldig poeng")