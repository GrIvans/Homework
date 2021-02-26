def f(x):
    return ((not(x < 5) or (x < 3)) and ((not(x < 2) or (x < 1))))


for i in range(1, 5):
    print(i, f(i))
#ans--2 verno
