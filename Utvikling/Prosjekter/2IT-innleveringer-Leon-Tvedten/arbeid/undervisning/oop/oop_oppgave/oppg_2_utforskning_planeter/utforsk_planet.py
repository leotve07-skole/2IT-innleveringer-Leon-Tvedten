class Romfartøy:
    def __init__(self, navn, hastighet, drivstoffmengde):
        self.navn = navn
        self.hastighet = hastighet
        self.drivstoffmengde = drivstoffmengde
    
    def presenter(self):
        print(f"{self.navn} har en hastighet på {self.hastighet}, og en drivstoffmengde på {self.drivstoffmengde}.")

    def øk_hastighet(self):
        if(self.drivstoffmengde > 0):
            self.hastighet += 1
            self.drivstoffmengde -= 1
        else:
            print(f"{self.navn} har ikke drivstoff.")
    

class Transportromfartøy(Romfartøy):
    def __init__(self, navn, hastighet, drivstoffmengde, transport_lager_areal):
        super().__init__(navn, hastighet, drivstoffmengde)
        self.transport_lager_areal = transport_lager_areal
    def presenter(self):
        return (f"{self.navn} er et romfartøy ment for å transportere austronauter. {self.navn} har en hastighet på {self.hastighet}, og en medium drivstoffmengde på {self.drivstoffmengde}. {self.navn} har også en stor transport lager på areal {self.transport_lager_areal}\n")

class Utforskerromfartøy(Romfartøy):
    def __init__(self, navn, hastighet, drivstoffmengde, utforsker_kamera):
        super().__init__(navn, hastighet, drivstoffmengde)
        self.utforsker_kamera = utforsker_kamera

    def presenter(self):
        return (f"{self.navn} er et romfartøy ment for å utforske planetoverflaten. {self.navn} har en middel hastighet på {self.hastighet}, og en stor drivstoffmengde på {self.drivstoffmengde}. {self.navn} har en utforsker kamera : {self.utforsker_kamera}\n")

class Undersøkerromfartøy(Romfartøy):
    def __init__(self, navn, hastighet, drivstoffmengde, undersøker_kamera):
        super().__init__(navn, hastighet, drivstoffmengde)
        self.undersøker_kamera = undersøker_kamera

    def presenter(self):
        return (f"{self.navn} er et romfartøy ment for å undersøke planeter fra verdensrommet. {self.navn} har en hastighet på {self.hastighet}, og en drivstoffmengde på {self.drivstoffmengde}. {self.navn} har en undersøker kamera : {self.undersøker_kamera}\n")


transport_fartøy = Transportromfartøy("Transport Romfartøy", 300, 350, 500)
utforsker_fartøy = Utforskerromfartøy("Utforsker Romfartøy", 130, 330, "16k ultra close up zoom camera 200 mm - 700 mm")
undersøker_fartøy = Undersøkerromfartøy("Undersøker Romfartøy", 260, 400, "32k ultra zoom 200 mm - 20000 mm")

print(transport_fartøy.presenter())
print(utforsker_fartøy.presenter())
print(undersøker_fartøy.presenter())