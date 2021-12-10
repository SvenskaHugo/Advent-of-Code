import math
f = open('2021-10.txt')
f = f.readlines()
s = {'(':1,'[':2,'{':3,'<':4}
o = ['(','[','{','<']
c = [')',']','}','>']
d = {'(':')','[':']','{':'}','<':'>'}
r = []
p = []
for i,x in enumerate(f):
	l = []
	for y in x.strip():
		if y in o:
			l.append(y)
		elif y in c:
			if d[l[len(l)-1]] == y:
				del l[len(l)-1]
			else:
				r.append(i)
				break
r.reverse()
for x in r:
	del f[x]
for x in f:
	l = []
	for y in x.strip():
		if y in o:
			l.append(y)
		elif y in c:
			if d[l[len(l)-1]] == y:
				del l[len(l)-1]
			else:
				break
	l.reverse()
	tp = 0
	for y in l:
		tp *= 5
		tp += s[y]
	p.append(tp)
p.sort()
print(p)
print(p[math.floor(len(p)/2)])