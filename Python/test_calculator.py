import pytest
from calculator import square

def test_positve():
    assert square(2) == 4
    assert square(3) == 9
 
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def tes_str():
    with pytest.raises(TypeError):
        square("cat")
