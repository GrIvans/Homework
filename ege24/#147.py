s = open('24data/24-s2.txt').read()
dict = {}
for i in range(1, len(s)):
    if s[i - 1] == 'A':
        dict[s[i]] = dict.get(s[i], 0) + 1

print(sorted(dict, key=dict.get, reverse=1)[0])
print(dict['L'])
# ans==L 1567
