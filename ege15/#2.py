def f(x):
    return not((x > 3) or (x < 3)) or (x < 1)


for i in range(1, 5):
    print(i, f(i))
#ans--3 verno