f = open('2021-3.txt')
f = f.readlines()
ox = f
g = open('2021-3.txt')
g = g.readlines()
co2 = g

for x in range(12):
	c0 = 0
	c1 = 0
	for y in ox:
		if y[x] == '1':
			c1 += 1
		else:
			c0 += 1
	d = []
	if c0 <= c1:
		for y in range(len(ox)):
			if ox[y][x] != '1':
				d.append(y)
	else:
		for y in range(len(ox)):
			if ox[y][x] != '0':
				d.append(y)
	d.reverse()
	for y in d:
		del ox[y]
	if len(ox) == 1:
		break

for x in range(12):
	c0 = 0
	c1 = 0
	for y in co2:
		if y[x] == '1':
			c1 += 1
		else:
			c0 += 1
	d = []
	if c0 <= c1:
		for y in range(len(co2)):
			if co2[y][x] != '0':
				d.append(y)
	else:
		for y in range(len(co2)):
			if co2[y][x] != '1':
				d.append(y)
	d.reverse()
	for y in d:
		del co2[y]
	if len(co2) == 1:
		break
ox.reverse()
co2.reverse()
print(ox)
print(co2)