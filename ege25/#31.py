def f(N):
    D = []
    if (N*0.5).is_integer():
        D = [d for d in range (1, N // 2 + 1) if N % d == 0] + [N]
    return D

for i in range(1820348, 2880927 + 1):
    a = f(i)
    if len(a) == 5:
        print(a)

