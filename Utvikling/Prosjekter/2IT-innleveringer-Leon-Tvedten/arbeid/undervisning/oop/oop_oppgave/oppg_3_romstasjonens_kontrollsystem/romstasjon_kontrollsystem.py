import sys
import os
arbeid_mappe = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../')) # Hente riktig fil plasseren i prosjekter for å hente terminal_style
sys.path.append(arbeid_mappe)
from terminal_styling.terminal_style import style # Style terminalens farger
class Romstasjonenhet:
   def __init__(self, navn):
       self.navn = navn

   def utfor_oppdrag(self):
      pass
class Satelitt(Romstasjonenhet):
    def __init__(self, navn):
        super().__init__(navn)
    def utfor_oppdrag(self):
        return (
                f"{style["g"]}----------------------------------------------------------------------------\n"
                f"{style["g"]}{self.navn} utfører oppdrag: bilde av verdensrommet\n"
                f"{style["g"]}----------------------------------------------------------------------------"
                )

class Robot(Romstasjonenhet):
    def __init__(self, navn):
            super().__init__(navn)
    def utfor_oppdrag(self):
        return (
                f"{style["g"]}----------------------------------------------------------------------------\n"
                f"{style["g"]}{self.navn} ufører oppdrag: reparere romstasjon\n"
                f"{style["g"]}----------------------------------------------------------------------------"
                )

class Kamera(Romstasjonenhet):
    def __init__(self, navn):
        super().__init__(navn)
    def utfor_oppdrag(self):
        return (
                f"{style["g"]}----------------------------------------------------------------------------\n"
                f"{style["g"]}{self.navn} utfører oppdrag: filme verdensrommet\n"
                f"{style["g"]}----------------------------------------------------------------------------"
                )
    

enheter = [
    Satelitt("Satelitt V1"),
    Satelitt("Satelitt V2"),
    Robot("Robot"), 
    Kamera("Kamera 16k"),
    Kamera("Kamera 32k")
    ]

for n in enheter:
    print(n.utfor_oppdrag())