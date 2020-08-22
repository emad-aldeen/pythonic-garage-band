from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Band, Musician, Guitarist, Drummer, Bassist
import pytest
def test_version():
    assert __version__ == '0.1.0'
# @pytest.mark.skip(reason='Testing Count')
# def test_play_solos():
#     ali = Band.Guitarist('ali') # preparing data
#     ahmad = Band.Drummer('ahmad')
#     soso = Band.Bassist('soso')
#     expected = "ali play solo\nahmad play solo\nsoso play solo\n"
#     actual = soso.play_solos()
#     assert actual == expected
aziz = Guitarist('Aziz') 
saleh = Drummer('Saleh')
emad = Bassist('Emad')    
tarbanin = Band('tarbanin')
tarbanin.add_members(aziz)
tarbanin.add_members(saleh)
tarbanin.add_members(emad)
# @pytest.fixture 
# def prep_data():
#     aziz = Band.Guitarist('Aziz') # preparing data
#     saleh = Band.Drummer('Saleh')
#     emad = Band.Bassist('Emad')
#     #preparing data
#     return {'aziz':aziz, 'saleh':saleh, 'emad':emad}
def test_to_list():
    expected = [aziz,saleh,emad]
    actual = tarbanin.to_list()
    assert  actual == expected
# @pytest.mark.skip(reason='Testing Count')
def test_play_solo():
    expected = 'Saleh Play solo'
    actual = saleh.play_solo()
    assert actual == expected
# @pytest.mark.skip(reason='Testing Count')
def test_play_solos():
    expected = "Aziz Play solo\nSaleh Play solo\nEmad Play solo\n"
    actual = tarbanin.play_solos()#because I called prep_data three times
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