def Szamolas(a,b,c):
    return a + b - c


def Teszteles():
    assert Szamolas(3,4,2) == 5
    assert Szamolas(3,3,5) == 2