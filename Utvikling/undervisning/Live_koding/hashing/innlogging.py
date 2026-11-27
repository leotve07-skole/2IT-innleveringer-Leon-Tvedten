import hashlib
import secrets

brukernavn = "admin"
passord = "Mars2027"

salt = secrets.token_bytes(16)
print("Salt:", salt)

hashverdi = hashlib.md5(salt + passord.encode()).hexdigest()

print(hashverdi)

#Input for brukernavn og passord
input_brukernavn = input("Skriv brukernavn : ")
input_passord = input("Skriv passord : ")

hashet_input = hashlib.md5(salt + input_passord.encode()).hexdigest()

if brukernavn == input_brukernavn and hashet_input == hashverdi:
    print("Login velykket!")
else:
    print("Hash verdi ikke funnet")