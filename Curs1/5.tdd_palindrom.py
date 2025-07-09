

def este_palindrom_v1(cuvant):
    return cuvant == cuvant[::-1]
   
def este_palindrom_v2(cuvant):
    return cuvant == "".join(reversed(cuvant))

def este_palindrom(cuvant):
    return all(cuvant[i] == cuvant[-1-i] for i in range(len(cuvant) // 2))

def test_palindrom():
    assert este_palindrom("kayak") == True, "Acest cuvant este palindrom"
    assert este_palindrom("masina") == False, "Acest cuvant NU este palindrom"


test_palindrom()