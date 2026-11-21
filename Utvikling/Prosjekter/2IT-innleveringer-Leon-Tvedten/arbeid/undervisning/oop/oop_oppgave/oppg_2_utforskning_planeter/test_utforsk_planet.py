from oppg_2_utforskning_planeter.utforsk_planet import Transportromfartøy, Utforskerromfartøy, Undersøkerromfartøy

def test_transport_romfartøy_får_felles_og_egne_attributter():
    transport_fartøy = Transportromfartøy("Transport Romfartøy", 300, 350, 500)

    assert transport_fartøy.navn == "Transport Romfartøy"
    assert transport_fartøy.hastighet == 300
    assert transport_fartøy.drivstoffmengde == 350
    assert transport_fartøy.transport_lager_areal == 500

    assert transport_fartøy.presenter() == "Transport Romfartøy er et romfartøy ment for å transportere austronauter. Transport Romfartøy har en hastighet på 300, og en medium drivstoffmengde på 350. Transport Romfartøy har også en stor transport lager på areal 500\n"
test_transport_romfartøy_får_felles_og_egne_attributter()

def test_utforsker_romfartøy_får_felles_og_egne_attributter():
    utforsker_fartøy = Utforskerromfartøy("Utforsker Romfartøy", 130, 330, "16k ultra close up zoom camera 200 mm - 700 mm")

    assert utforsker_fartøy.navn == "Utforsker Romfartøy"
    assert utforsker_fartøy.hastighet == 130
    assert utforsker_fartøy.drivstoffmengde == 330
    assert utforsker_fartøy.utforsker_kamera == "16k ultra close up zoom camera 200 mm - 700 mm"

    assert utforsker_fartøy.presenter() == "Utforsker Romfartøy er et romfartøy ment for å utforske planetoverflaten. Utforsker Romfartøy har en middel hastighet på 130, og en stor drivstoffmengde på 330. Utforsker Romfartøy har en utforsker kamera : 16k ultra close up zoom camera 200 mm - 700 mm\n"
test_utforsker_romfartøy_får_felles_og_egne_attributter()
def test_undersoker_romfartøy_får_felles_og_egne_attributter():
    undersøker_fartøy = Undersøkerromfartøy("Undersøker Romfartøy", 260, 400, "32k ultra zoom 200 mm - 20000 mm")

    assert undersøker_fartøy.navn == "Undersøker Romfartøy"
    assert undersøker_fartøy.hastighet == 260
    assert undersøker_fartøy.drivstoffmengde == 400
    assert undersøker_fartøy.undersøker_kamera == "32k ultra zoom 200 mm - 20000 mm"

    assert undersøker_fartøy.presenter() == "Undersøker Romfartøy er et romfartøy ment for å undersøke planeter fra verdensrommet. Undersøker Romfartøy har en hastighet på 260, og en drivstoffmengde på 400. Undersøker Romfartøy har en undersøker kamera : 32k ultra zoom 200 mm - 20000 mm\n"
test_undersoker_romfartøy_får_felles_og_egne_attributter()