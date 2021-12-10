f = open('2021-2.txt')
f = f.readlines()
h = 0
d = 0
a = 0
for x in f:
	if x.split(' ')[0] == 'forward':
		h += int(x.split(' ')[1])
		d += int(x.split(' ')[1]) * ae
	elif x.split(' ')[0] == 'down':
		a += int(x.split(' ')[1])
	elif x.split(' ')[0] == 'up':
		a -= int(x.split(' ')[1])
print(h*d)