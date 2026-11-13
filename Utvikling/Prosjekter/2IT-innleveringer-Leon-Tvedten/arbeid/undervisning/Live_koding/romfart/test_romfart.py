import pytest
from romfart import beregn_avstand, beregn_drivstoff, velkommen

@pytest.mark.parametrize("fart,timer,forventet", 
                         [
                             (1000, 5,5000),
                             (2000, 10, 20000),
                             (1000,0,0)
                         ])
def test_beregn_avstand(fart, timer, forventet):
    # assert beregn_avstand(1000, 5) == 5000, "Feil avstand beregnet"
    assert beregn_avstand(fart, timer) == forventet

def test_beregn_drivstoff():
    assert beregn_drivstoff(1000, 4) == 4000, "Feil drivstoff beregnet"

def test_avstand_med_null_timer_er_nulloka():
    assert beregn_avstand(1000, 0) == 0

def test_beregn_avstand_med_mindre_enn_null_timer():
    with pytest.raises(ValueError):
        beregn_avstand(1000, -5)

def test_desimaltall():
    assert 0.1 + 0.2 == pytest.approx(0.3)

def test_velkommen():
    assert velkommen("Leon") == "Velkommen om bord Leon"