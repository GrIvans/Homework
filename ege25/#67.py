def chet(a):
    if a % 2 == 0:
        return True
    return False


def f(a):
    c = str(a)
    if chet(int(c[2])) and chet(int(c[4])) and not(chet(int(c[0]))) and \
        not chet(int(c[1])) and not (chet(int(c[3]))):
        return True
    return False


def Delit(a):
    if (a % 6) != 0 and a % 7 != 0 and a % 8 != 0:
        return True
    return False


a = [n for n in range(33333, 55556)
if f(n) and Delit(n)]
print(len(a), max(a) - min(a))
