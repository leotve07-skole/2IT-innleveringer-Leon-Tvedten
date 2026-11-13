class Dyreparken:
    def __init__(self, dyrepasser, navn, alder, dyre_art, spise_måte):
        self.dyrepassser = dyrepasser
        self.navn = navn
        self.alder = alder
        self.dyre_art = dyre_art
        self.spise_måte = spise_måte

class Bjørn(Dyreparken):
    def __init__(self, navn, spise_måte):
        super().__init__(navn, spise_måte)

    def spise_måte(self):
         print(f"{self.navn} sin spise måte er {self.spise_måte}")


class Rovdyr(Dyreparken):
    def __init__(self, navn, spise_måte):
        super().__init__(navn, spise_måte)

    def spise_måte(self):
        print(f"{self.navn} sin spise måte er {self.spise_måte}")

class Elg(Dyreparken):
    def __init__(self, navn, spise_måte, horn_lengde):
        super().__init__(navn, spise_måte)
        self.horn_lengde = horn_lengde
    def spise_måte(self):
        print(f"{self.navn} sin spise måte er {self.spise_måte}")
