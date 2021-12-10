f = open('2021-8.txt')
f = f.readlines()
c = 0
segments = ['a','b','c','d','e','f','g']
for x in f:
	p = x.split('|')[0]
	o = x.split('|')[1]
	count = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0}
	for y in p.split(' '):
		for z in list(y):
			count[z] += 1
	for y in p.split(' '):
		if len(y) == 2:
			one = list(y)
		elif len(y) == 3:
			seven = list(y)
		elif len(y) == 4:
			four = list(y)
		elif len(y) == 7:
			eight = list(y)
	for z in seven:
		if z not in one:
			s1 = z
	for y in p.split(' '):
		if len(y) == 6:
			for z in segments:
				if z in one and z not in list(y):
					s3 = z
	for y in list(count.keys()):
		if count[y] == 9:
			s6 = y
		elif count[y] == 6:
			s2 = y
		elif count[y] == 4:
			s5 = y
		for z in four:
			if y in four and count[y] == 7:
				s4 = y
			elif y not in four and count[y] == 7:
				s7 = y
		numbers = []
	for y in o.split(' '):
		if len(y.strip()) == 6 and s4 not in list(y):
			numbers.append(0)
		elif len(y.strip()) == 2:
			numbers.append(1)
		elif len(y.strip()) == 5 and s2 not in list(y) and s6 not in list(y):
			numbers.append(2)
		elif len(y.strip()) == 5 and s2 not in list(y) and s5 not in list(y):
			numbers.append(3)
		elif len(y.strip()) == 4:
			numbers.append(4)
		elif len(y.strip()) == 5 and s3 not in list(y) and s5 not in list(y):
			numbers.append(5)
		elif len(y.strip()) == 6 and s3 not in list(y):
			numbers.append(6)
		elif len(y.strip()) == 3:
			numbers.append(7)
		elif len(y.strip()) == 7:
			numbers.append(8)
		elif len(y.strip()) == 6 and s5 not in list(y):
			numbers.append(9)
	c += (numbers[0] * 1000) + (numbers[1] * 100) + (numbers[2] * 10) + numbers[3]
print(c)