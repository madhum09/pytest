import pytest

def test_m1():
    a=4
    b=3
    assert a+1==b, "test got failed"

def test_m2():
    name="madhu"
    assert name.upper()=="MADHU"

def test_m3():
    name="madhu"
    assert name.upper()=="MADU", "test got failed"

def test_m4():
   assert True  
