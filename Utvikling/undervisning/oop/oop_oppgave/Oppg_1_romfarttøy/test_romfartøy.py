from Oppg_1_romfarttøy.romfartøy import Romfartøy
import pytest

@pytest.mark.parametrize("start_drivstoff, forventet_hastighet, forventet_drivstoff", [
    (120, 701, 119),
    (0, 700, 0),
    (1, 701, 0),
])
def test_romfartøy_øk_hastighet(start_drivstoff, forventet_hastighet, forventet_drivstoff):
    test_fartøy = Romfartøy("Test Romfartøy", 700, start_drivstoff, 45)

    test_fartøy.øk_hastighet()
    
    assert test_fartøy.hastighet == forventet_hastighet
    assert test_fartøy.drivstoffmengde == forventet_drivstoff

def test_romfartøy_ikke_bruker_mer_drivstoff_en_det_har():
    test_fartøy = Romfartøy("Test Romfartøy", 700, 0, 45)

    test_fartøy.øk_hastighet()

    assert test_fartøy.hastighet == 700
    assert test_fartøy.drivstoffmengde == 0

def test_romfartøy_drivstoff_grense_tilfelle():
    test_fartøy = Romfartøy("Test Romfartøy", 700, 1, 45)

    test_fartøy.øk_hastighet()

    assert test_fartøy.hastighet == 701
    assert test_fartøy.drivstoffmengde == 0

  