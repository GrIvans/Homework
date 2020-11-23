fout = open('output.txt', 'w')
with open('input.txt') as text:
    number = 1
    for line in text:
        word = ''
        for sim in line:
            if 'a' <= sim <= 'z':
                next_sim = ord('a') + ((ord(sim) + number - ord('a'))  % 26)
            elif 'A' <= sim <= 'Z':
                next_sim = ord('A') + ((ord(sim) + number - ord('A'))  % 26)
            else:
                next_sim = ord(sim)
            word += (chr(next_sim)) 
        number += 1
        fout.write(word)
        word = ''
fout.close()
