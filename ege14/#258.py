def kol(i):
    k = 0
    a = 456
    while a != 0:
        if (a % i) % 2 == 1:
            k += 1
        a //= i
    return k


mx = 0
ans = 0
for i in range(2, 11):
    if kol(i) >= mx:
        mx = kol(i)
        ans = i
print(ans)
# ans==5 verno
