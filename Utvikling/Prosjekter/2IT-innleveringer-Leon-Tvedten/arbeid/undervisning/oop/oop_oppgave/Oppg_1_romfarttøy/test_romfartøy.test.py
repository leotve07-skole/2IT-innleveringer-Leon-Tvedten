from Oppg_1_romfarttøy.romfartøy import Romfartøy


def test_romfartøy_øk_hastighet():
    test_fartøy = Romfartøy("Test Romfartøy", 700, 120, 45)

    test_fartøy.øk_hastighet()
    
    assert test_fartøy.hastighet == 701
    assert test_fartøy.drivstoffmengde == 119

def test_romfartøy_ikke_bruker_mer_drivstoff_en_det_har():
    test_fartøy = Romfartøy("Test Romfartøy", 700, 0, 45)

    test_fartøy.øk_hastighet()

    assert test_fartøy.hastighet == 700
    assert test_fartøy.drivstoffmengde == 0

