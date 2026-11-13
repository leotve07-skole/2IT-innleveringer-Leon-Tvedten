class Romfartøy:
    def __init__(self, navn, hastighet, drivstoffmengde, bredde_og_hoyde):
        self.navn = navn
        self.hastighet = hastighet
        self.drivstoffmengde = drivstoffmengde
        self.bredde_og_hoyde = bredde_og_hoyde
    
    def presenter(self):
        print(f"{self.navn} har en hastighet på {self.hasitghet}, og en drivstoffmengde på {self.drivstoffmengde}. {self.navn} har en areal på {self.bredde_og_hoyde}")

    def øk_hastighet(self):
        if(self.drivstoffmengde > 0):
            self.hastighet += 1
            self.drivstoffmengde -= 1
        else:
            print(f"{self.navn} har ikke drivstoff.")
    

class Raskfartøy(Romfartøy):
    def __init__(self, navn, hastighet, drivstoffmengde, bredde_og_hoyde, thrust_areal):
        super().__init__(navn, hastighet, drivstoffmengde, bredde_og_hoyde)
        self.thrust_areal = thrust_areal

    def presenter(self):
        print(f"{self.navn} har en rask hastighet på {self.hastighet}, og en medium stor drivstoffmengde på {self.drivstoffmengde}. {self.navn} har også thruster for å øke hastigheten, arealet til thrustene er {self.thrust_areal}. Arealet til {self.navn} er {self.bredde_og_hoyde}, som er lite.\n")

class Distansefartøy(Romfartøy):
    def __init__(self, navn, hastighet, drivstoffmengde, bredde_og_hoyde, tank_areal):
        super().__init__(navn, hastighet, drivstoffmengde, bredde_og_hoyde)
        self.tank_areal = tank_areal

    def presenter(self):
        print(f"{self.navn} har en middel hastighet på {self.hastighet}, og en stor drivstoffmengde på {self.drivstoffmengde}. {self.navn} har også en stor tank til drivstoff, arealet til tanken er {self.tank_areal}. Arealet til {self.navn} er {self.bredde_og_hoyde} som er medium stort.\n")

class Stortfartøy(Romfartøy):
    def __init__(self, navn, hastighet, drivstoffmengde, bredde_og_hoyde, lager_plass_areal):
        super().__init__(navn, hastighet, drivstoffmengde, bredde_og_hoyde)
        self.lager_plass_areal = lager_plass_areal

    def presenter(self):
        print(f"{self.navn} har en hastighet på {self.hastighet}, og en drivstoffmengde på {self.drivstoffmengde}. {self.navn} har også en stor lagerplass på fartøyet som har et areal på {self.lager_plass_areal}. Arealet til {self.navn} er {self.bredde_og_hoyde} som er et stort fartøy.\n")


rask_fartøy = Raskfartøy("Rask Romfartøy", 700, 120, 45, 10)
distanse_fartøy = Distansefartøy("Distanse Romfartøy", 350, 600, 340, 150)
stort_fartøy = Stortfartøy("Stort Romfartøy", 190, 800, 2540, 500)

rask_fartøy.presenter()
distanse_fartøy.presenter()
stort_fartøy.presenter()