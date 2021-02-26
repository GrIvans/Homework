k = 0
for x in range(1001):
    for y in range(1001):
        if (not((x > 5) or ((x + y) >= 4) or (y >= 5))) == True:
            k += 1
print(k)
# ans--10 verno
