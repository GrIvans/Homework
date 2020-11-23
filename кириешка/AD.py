s = open('input.txt')
four = open('output.txt', 'w')
y = s.readline()
votes = {}
parties = []
while True:
    y = s.readline()
    if y != 'VOTES:\n':
        parties.append(y)
    else:
        break
for i in sorted(parties):
    votes[i] = 0
while True:
    y = s.readline()
    if y != '':
        votes[y] += 1
    else:
        break
for i in (sorted(votes, key=votes.get, reverse=1)):
    print(i[:-1])
    