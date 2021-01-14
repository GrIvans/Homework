def unic(a):
    s = str(a)
    if not (chet(int(s[0]))) and not (chet(int(s[1]))) and \
        (chet(int(s[2]))) and (chet(int(s[3]))) and (chet(int(s[4]))):
        return True
    return False


def chet(a):
    if a % 2 == 0:
        return True
    return False


def delit(a):
    if a % 7 != 0 and a % 9 != 0 and a % 13 != 0:
        return True
    return False


a = [n for n in range(57888, 74556)
if unic(n) and delit(n)]
print(len(a), max(a) - min(a))
