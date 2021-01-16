def Delit(a):
    global delit
    for i in delit:
        if a % i == 0:
            return False
    return True


delit = []


def Del():
    global delit
    i = 2
    while i**2 <= 18300:
        delit.append(i**2)
        i += 1

def summCifr(a):
    sm = 0
    while a != 0:
        sm += a % 10
        a //= 10
    return sm
     

Del()
sm = 0
for i in range(2945, 18294 + 1):
    if Delit(i):
        sm += summCifr(i)
print(sm)
