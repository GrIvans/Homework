def f(i):
    a = 3456
    while a != 0:
        if (a % i) % 2 == 1:
            return False
        a //= i
    return True


sm = 0
for i in range(2, 11):
    if f(i):
        sm += i
print(sm)
# ans--23 verno
