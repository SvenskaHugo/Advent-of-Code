import time
f = open('2021-6.txt')
f = f.readlines()
f = f[0].split(',')
l = []
d = 0
b = [0,0]
for x in f:
	l.append(int(x))
while d != 256:
	d += 1
	b = [0,8]
	for i,x in enumerate(l):
		if type(x) == list:
			if x[1] == 0:
				b[0] += x[0]
				x[1] = 6
			else:
				x[1] -= 1
		elif x == 0:
			b[0] += 1
			l[i] = 6
		else:
			l[i] -= 1
	l.append(b)
c = 0
for x in l:
	if type(x) == list:
		c += x[0]
	else:
		c += 1
print(c)