f = open('2021-10.txt')
fc = f.copy()
s = {')':3,']':57,'}':1197,'>':25137}
o = ['(','[','{','<']
c = [')',']','}','>']
d = {'(':')','[':']','{':'}','<':'>'}
p = 0
for x in f:
	l = []
	for y in x:
		if y in o:
			l.append(y)
		elif y in c:
			if d[l[len(l)-1]] == y:
				del l[len(l)-1]
			else:
				p += s[y]
				break
print(p)