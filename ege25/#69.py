def chet(a):
    if a % 2 == 0: 
        return True
    return False


def unic(a):
    s = str(a)
    if chet(int(s[0])) and chet(int(s[1])) and \
        not chet(int(s[2])) and not chet(int(s[3])) and \
            not chet(int(s[4])):
            return True
    return False


def delit(a):
    if a % 9 != 0 and a % 13 != 0 and a % 17 != 0:
        return True
    return False


a = [n for n in range(64444, 77564)
if unic(n) and delit(n)]
print(len(a), max(a) - min(a))
