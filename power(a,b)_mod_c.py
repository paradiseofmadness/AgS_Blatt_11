import random


def modpower(a, b, n):
    res = 1
    faktor = 1
    binärzahl = bin(b).split("b")[1]
    for i in range(len(binärzahl)):
        if binärzahl[i] == '1':
            res = (res * faktor) % n
        faktor = faktor ** 2
    return res


for _ in range(10):
    a, b, n = random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000)
    print(f"{a}^{b} mod {n} = {modpower(a, b, n)}")
