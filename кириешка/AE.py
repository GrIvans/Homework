s = open('input.txt', encoding='utf-8').readlines()
votes = {}
kol = len(s)
for vote in s:
    votes[vote] = votes.get(vote, 0) + 1
for i in votes:
    votes[i] = votes[i] / kol
vt = sorted(votes, key=votes.get, reverse=1)
if votes[vt[0]] > 0.5:
    print(vt[0])
else:
    print(vt[0], vt[1], sep='')