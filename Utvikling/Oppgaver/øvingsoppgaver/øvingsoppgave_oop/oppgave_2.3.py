class Fotballklubb:
    def __init__(self, klubb, region, trener):
        self.klubb = klubb
        self.region = region
        self.trener = trener

class Fotballspillere(Fotballklubb):
    def spillere(self, klubb, region, navn, alder, erfaring):
        super().__init__(klubb, region)
        self.navn = navn
        self.alder = alder
        self.erfaring = erfaring

class Fotballbane(Fotballklubb):
    def bane(self, klubb, region):
       super().__init__(klubb, region)

class Skadet_spillere(Fotballspillere):
    def spillere(self, navn, alder, erfaring, skade_grad):
        super().__init__(navn, alder, erfaring)
        self.skade_grad = skade_grad