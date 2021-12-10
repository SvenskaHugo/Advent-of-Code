f = open('2020-3.txt')
f = f.readlines()
l = len(f)
print(l)
r = len(f[0].removesuffix('\n'))
p = 1
for a, b in zip([1,1,1,1,2], [1,3,5,7,1]):
	x = 0
	y = 0
	t = 0
	while x < l:
		if f[x][y] == '#':
			t += 1
		x += a
		y += b
		if r <= y:
			y -= r
	p *= t
print(p)