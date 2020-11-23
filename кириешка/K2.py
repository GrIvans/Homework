fin = open('input.txt')
fout = open('output.txt', 'w')
k = 0
for x in fin:
    k += 1
    s = ''
    for a in x:
        if 'a' <= a <= 'z':
            s += chr((ord(a) - ord('a') + k) % 26 + ord('a'))
        elif 'A' <= a <= 'Z':
            s += chr((ord(a) - ord('A') + k) % 26 + ord('A'))
        else:
            s += a
    fout.write(s)
fout.close()
