from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Band
# import pytest

def test_version():
    assert __version__ == '0.1.0'

# @pytest.mark.skip(reason='Testing Count')
# def test_play_solos():
#     ali = Band.Guitarist('ali') # preparing data
#     ahmad = Band.Drummer('ahmad')
#     soso = Band.Bassist('soso')
#     expected = "ali play a solos\nahmad play a solos\nsoso play a solos\n"
#     actual = soso.play_solos()
#     assert actual == expected

aziz = Band.Guitarist('Aziz') # preparing data
saleh = Band.Drummer('Saleh')
emad = Band.Bassist('Emad')   

# @pytest.fixture 
# def prep_data():
#     aziz = Band.Guitarist('Aziz') # preparing data
#     saleh = Band.Drummer('Saleh')
#     emad = Band.Bassist('Emad')
#     #preparing data
#     return {'aziz':aziz, 'saleh':saleh, 'emad':emad}

def test_to_list():
    expected = ['Aziz','Saleh','Emad']
    actual = aziz.to_list()
    assert  actual == expected

# @pytest.mark.skip(reason='Testing Count')
def test_play_solo():
    expected = 'Dom Dum Dom Dum'
    actual = saleh.play_solo()
    assert actual == expected

# @pytest.mark.skip(reason='Testing Count')
def test_play_solos():
    expected = "Aziz play a solos\nSaleh play a solos\nEmad play a solos\n"
    actual = aziz.play_solos()
    assert actual == expected

def test_str():
    expected = "Guitarist <Aziz>"
    actual = aziz.__str__()
    assert actual == expected

def test_rper():
    expected = " 'Emad' "
    actual = emad.__repr__()
    assert actual == expected

def test_get_instrument():
    expected = "Drummer"
    actual = saleh.get_instrument()
    assert actual == expected