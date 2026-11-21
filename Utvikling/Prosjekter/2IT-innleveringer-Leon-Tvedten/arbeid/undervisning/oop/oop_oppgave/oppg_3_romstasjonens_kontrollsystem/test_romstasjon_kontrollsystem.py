from oppg_3_romstasjonens_kontrollsystem.romstasjon_kontrollsystem import Satelitt, Robot, Kamera
from terminal_styling.terminal_style import style 

def test_utfor_oppdrag_satelitt():
    satelitt = Satelitt("Satelitt")

    assert satelitt.utfor_oppdrag() == (
                f"{style["g"]}----------------------------------------------------------------------------\n"
                f"{style["g"]}Satelitt utfører oppdrag: bilde av verdensrommet\n"
                f"{style["g"]}----------------------------------------------------------------------------"
                )
    
def test_utfor_oppdrag_robot():
   robot = Robot("Robot")
   assert robot.utfor_oppdrag() ==  (
                f"{style["g"]}----------------------------------------------------------------------------\n"
                f"{style["g"]}Robot utfører oppdrag: reparere romstasjon\n"
                f"{style["g"]}----------------------------------------------------------------------------"
                )
def test_utfor_oppdrag_kamera():
   kamera = Kamera("Kamera")

   assert kamera.utfor_oppdrag() == (
                f"{style["g"]}----------------------------------------------------------------------------\n"
                f"{style["g"]}Kamera utfører oppdrag: filme verdensrommet\n"
                f"{style["g"]}----------------------------------------------------------------------------"
                )