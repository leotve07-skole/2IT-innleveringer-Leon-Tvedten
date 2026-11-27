class Arbeider:
    def __init__(self, navn, yrke):
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