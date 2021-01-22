for a in range(1, 201):
    fl = True
    for x in range(1, 10000):
        if (120 % a) and ((not(x % 70 and x % 30) or x % a)) == 0:
            fl = False
    if fl:
        print(a)
#neverno
#ДЕЛ(120, A) /\ ((ДЕЛ(x, 70) /\ ДЕЛ(x, 30)) → ДЕЛ(x, A))
