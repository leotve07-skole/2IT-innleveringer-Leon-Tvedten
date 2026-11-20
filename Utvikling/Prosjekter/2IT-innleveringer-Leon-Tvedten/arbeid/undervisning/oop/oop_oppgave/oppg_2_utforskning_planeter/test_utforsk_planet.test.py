from oppg_2_utforskning_planeter.utforsk_planet import Transportromfartøy, Utforskerromfartøy, Undersøkerromfartøy

def test_transport_romfartøy_får_felles_og_egne_attributter():
    transport_fartøy = Transportromfartøy("Transport Romfartøy", 300, 350, 500)

    assert transport_fartøy.navn == "Transport Romfartøy"
    assert transport_fartøy.hastighet == 300
    assert transport_fartøy.drivstoffmengde == 350
    assert transport_fartøy.transport_lager_areal == 500
