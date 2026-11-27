import hashlib
import secrets

brukernavn = ["Admin", "Bruker12", "Bruker32"]
passord_hash = []
kommando = ["Registrer", "Login"]

salt = secrets.token_bytes(16)

while True:
    bruker_input = input("Skriv Registrer eller Login\n")
    match bruker_input:
        case "register":
            registrer_brukernavn = input("Skriv brukernavn : ")
            registrer_passord = input("Skriv passord : ")

            if registrer_brukernavn not in brukernavn:
                brukernavn.append(registrer_brukernavn)
                passord_hash.append(hashlib.md5(salt + registrer_passord.encode()).hexdigest())
                print("Registrering velykket!")
            else:
                print("Brukernavn allerede registrert")
        case "login":
            login_brukernavn = input("Skriv brukernavn : ")
            login_passord_hash = hashlib.md5(salt + input("Skriv passord : ").encode()).hexdigest()
            if login_brukernavn in brukernavn and login_passord_hash in passord_hash:
                print("Login velykket!")
            else :
                print("Feil passord eller brukernavn")

