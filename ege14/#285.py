def f(i):
    a = 437
    s = ''
    while a != 0:
        s += str(a % i)
        a //= i
    return sum(map(int, s[::-1]))


ans = 0
for i in range(2, 11):
    s = f(i)
    if s % 2 == 0:
        ans += i
print(ans)
