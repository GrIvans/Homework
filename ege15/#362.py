k = 0
for x in range(1, 501):
    for y in range(1, 501):
        if (not(((x > 1) and ((x + y) >= 6)) or (y >= 5))) == True:
            k += 1
print(k)
# ans--10 verno
