k = 0
for x in range(1, 1001):
    for y in range(1, 1001):
        if (not((x > 5) or ((x + y) >= 4) and (y >= 5))) == True:
            k += 1
print(k)
# ans--20 neverno (10)
