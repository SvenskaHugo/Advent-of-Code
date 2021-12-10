f = open('2021-1.txt')
f = f.readlines()
c = 0
for i, d in enumerate(f[1:]):
	a = int(f[i].removesuffix('\n'))
	b = int(d.removesuffix('\n'))
	if a < b:
		c += 1
print(c)