

def adunare(a, b):
    return a + b 


def test_adunare():
    assert adunare(2, 3) == 5
    assert adunare(0, -1) == -1

test_adunare()