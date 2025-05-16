import pytest

@pytest.mark.login
def test_m8():
    name="madhu"
    assert name.upper()=="MADHU"

@pytest.mark.login
def test_m9():
    name="madhu"
    assert name.upper()=="MADHU", "test got failed"

def test_m10():
   assert True  


def test_m10():
   assert False     