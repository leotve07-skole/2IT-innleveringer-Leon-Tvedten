def satelitt_melding(satelitt, planet):
    return(
            "---------------------\n"
            f"Satelitt: {satelitt}\n{satelitt} er på planet: {planet}\n"
            "---------------------"

        )
print(satelitt_melding("12_s", "Mars"))
print(satelitt_melding("12_f", "Jupiter"))
print(satelitt_melding("12_q", "Jord"))
def regn_signal_tid(distanse):
    radio_bølge_fart = 300 * 1000
    return (distanse * 1000) / radio_bølge_fart

print(regn_signal_tid(200))
print(regn_signal_tid(143203))

signal_tid = regn_signal_tid(900)
print(f"Signal tid er {signal_tid} sekunder")
if signal_tid < 1:
    print("Direkte kommunikasjon")
elif signal_tid < 10:
    print("Forskinket kommunikasjon")
else:
    print("Stor signalforsinkelse")

def meteor_varsel(diameter, distanse_fra_jorden):
    if diameter > 500 and distanse_fra_jorden < 10000:
        return "Høy risiko"
    elif diameter > 300 and distanse_fra_jorden < 20000:
        return "Middels risiko"
    else:
        return "Lav risiko"

print(meteor_varsel(500, 1000))
print(meteor_varsel(2500, 1000))
print(meteor_varsel(5000, 2000000))