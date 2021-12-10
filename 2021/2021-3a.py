f = open('2021-3.txt')
f = f.readlines()
g = []
e = []
for x in range(12):
	g.append(None)
	e.append(None)
for x in range(12):
	c0 = 0
	c1 = 1
	for y in f:
		if y[x] == '0':
			c0 += 1
		else:
			c1 += 1
	if c0 < c1:
		g[x] = 1
		e[x] = 0
	else:
		g[x] = 0
		e[x] = 1
a = 0
p = 0
g.reverse()
e.reverse()
for x in range(12):
	a += g[x] * (2 ** x)
	p += e[x] * (2 ** x)
print(a*p)