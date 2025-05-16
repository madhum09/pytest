import pytest

def test_m5():
    name="madhu"
    assert name.upper()=="MADHU"

def test_m6():
    name="madhu"
    assert name.upper()=="MADU", "test got failed"

def test_m7():
   assert True  