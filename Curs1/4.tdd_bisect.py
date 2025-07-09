


def este_bisect(an):
    if an % 400 == 0 or (an % 100 != 0 and an % 4 == 0):
        return True
    else:
        return False

def test_este_bisect():
    assert este_bisect(2000) == True, "Anul 2000 este bisect"
    assert este_bisect(2001) == False, "Anul 2001 NU este bisect"
    assert este_bisect(1996) == True, "Anul 1996 este bisect"
    assert este_bisect(2100) == False, "Anul 2100 NU este bisect"

test_este_bisect()