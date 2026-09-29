
# fil = open("planeter.txt", "w")
#fil.write("Mars\n")
#fil.close()

#with open("planeter.txt", "r") as fil:
 #   for linje in fil:
  #      print(linje)


planet = input("Skriv inn en planet")

with open("planeter.txt", "w") as fil:
    fil.write(planet + "\n")
    
with open("planeter.txt", "r") as fil:
    fil.write(fil.read())

print("Planeten ble lagret")