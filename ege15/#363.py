k = 0
for x in range(1, 1001):
    for y in range(1, 1001):
        if (not(((x > 6) and ((x + y) >= 5)) or (y >= 5))) == True:
            k += 1
print(k)
# ans--24 neverno (35)
