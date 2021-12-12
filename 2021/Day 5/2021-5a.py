f = open('2021-5.txt')
f = f.readlines()
b = []
for x in range(1000):
	b.append([])
	for y in range(1000):
		b[x].append(0)
for x in f:
	l = x.split(' ')
	y1 = int(l[0].split(',')[0])
	x1 = int(l[0].split(',')[1])
	y2 = int(l[2].split(',')[0])
	x2 = int(l[2].split(',')[1])
	if (x1 != x2 and y1 != y2):
		continue
	if x1 != x2 and y1 == y2:
		for y in range(abs(x1-x2)+1):
			b[y1][min(x1,x2)+y] += 1
	elif y1 != y2 and x1 == x2:
		for y in range(abs(y1-y2)+1):
			b[min(y1,y2)+y][x1] += 1
c = 0
for x in b:
	for y in x:
		if y > 1:
			c += 1
print(c)