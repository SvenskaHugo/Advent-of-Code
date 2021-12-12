f = open('2021-6.txt')
f = f.readlines()
f = f[0].split(',')
l = []
d = 0
for x in f:
	l.append(int(x))
while d != 80:
	d += 1
	for i,x in enumerate(l):
		if x == 0:
			l.append(9)
			l[i] = 6
		else:
			l[i] -= 1
print(len(l))