f = open('2021-8.txt')
f = f.readlines()
c = 0
for x in f:
	l = x.split('|')[1]
	l = l.split(' ')
	for y in l:
		if len(y.strip()) in [2,3,4,7]:
			c += 1
print(c)