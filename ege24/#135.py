# не работает
s = open('input.txt').read()
s = s.replace('JBOSS', ' ')
s = s.replace('BOSSJ', ' ')
s = s.replace('JBOSSJ', ' ')
s = s.replace('BOSS', '1')
print(s.count('1'))
