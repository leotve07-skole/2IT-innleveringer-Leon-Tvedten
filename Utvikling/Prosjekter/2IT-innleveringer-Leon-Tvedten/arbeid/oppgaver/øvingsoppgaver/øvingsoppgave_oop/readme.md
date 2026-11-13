Oppgave 1.1
Fido lager en lyd
Katt lager en lyd
Ukjent lager en lyd
Egentlig output:
Fido sier voff
Pus lager en lyd
Ukjent lager en lyd

Ingen linje var så særlig vanskelig og forutsi men jeg tok feil på output fordi jeg la ikke fullt merke til at fido var printet ut med Hund class.
For å få katten til å oppføre seg som en katt ville jeg lagt til "Def lyd(self): print(self.navn, "sier mjau")" inne i Katt class.
Oppgave 1.2
class Kjoretoy:
def **init**(self, merke, aarsmodell):
self.merke = merke
self.aarsmodell = aarsmodell

    def info(self):
        print(self.merke, "fra", self.aarsmodell)

class Elbil(Kjoretoy):
def **init**(self, merke, aarsmodell, rekkevidde):
<- mangler self.merke = merke
<- mangler self.aarsmodell = aarsmodell
self.rekkevidde = rekkevidde

bil = Elbil("Tesla", 2021, 450)
bil.info()
Fikset:
class Kjoretoy:
def **init**(self, merke, aarsmodell):
self.merke = merke
self.aarsmodell = aarsmodell

    def info(self):
        print(self.merke, "fra", self.aarsmodell)

class Elbil(Kjoretoy):
def **init**(self, merke, aarsmodell, rekkevidde):
self.merke = merke
self.aarsmodell = aarsmodell
self.rekkevidde = rekkevidde

bil = Elbil("Tesla", 2021, 450)
bil.info()

Oppgave 1.3
Hund og dyr bør være arv fordi en hund er et type dyr.
Bil og Hjul trenger ikke å være arv fordi Hjul er i alle biler.
Elev og person trenger ikke å være arv fordi det kan være definert i person.
Bibliotek og bok trenger ikke å være arv fordi bok er i biblioteket.
Lærer og skole kan være arv fordi skole er skole kan være flere ting en bare lærer.
Kvadrat og rektangel passer ikke som arv fordi det er to ulike former.

Del 2

Oppgave 2.1

Alle har til felles at de er på skolen.
Elever er unikt med at de har en annen stilling på skolen en lærere og vaktmestere, som at de får karakterer, lekser og undervisning.
Lærerere er unikt fordi de har en lønn og de har stilling, og hvilken type lærer de er.
Vaktmestere er unikt fordi de har lønn og skifter.

De alle kunne hatt en metode på , presenter_skolens_representanter(), som viser, alder, navn, og stilling i skolen. Det som ville være forskjellig for hver av dem er alder, navn, og stilling forskjellig.
Jeg valgte attributt stilling fordi det er relevant for å vise hva en person gjør på skolen.

Oppgave 2.2
class Arbeider:
def **init**(self, navn, yrke):
self.navn = navn
self.yrke = yrke

class Snekker(Arbeider):
def jobb(self):
print(self.navn, "bygger et hus")

class Pilot(Arbeider):
def jobb(self):
print(self.navn, "flyr et fly")

class Lege(Arbeider):
def jobb(self):
print(self.navn, "behandler pasienter")

Oppgave 2.3
Det er nyttig med blandende objekter i mitt program fordi at det har forskjellige detaljer i en fotballklubb.

Del 3:
