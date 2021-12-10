f = open('2020-3.txt')
f = f.readlines()
x = 0
y = 0
l = len(f)
print(l)
t = 0
r = len(f[0].removesuffix('\n'))
while x < l:
	if f[x][y] == '#':
		t += 1
	x += 1
	y += 3
	if r <= y:
		y -= r
print(t)