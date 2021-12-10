f = open('2021-8.txt')
f = f.readlines()
c = 0
segments = ['a','b','c','d','e','f','g']
for x in f:
	p = x.split('|')[0]
	o = x.split('|')[1]
	for y in p.split(' '):		#find segment 1
		if len(y) == 2:
			one = list(y)
		elif len(y) == 3:
			seven = list(y)
	for z in seven:
		if z not in one:
			s1 = z
	print(s1)
	scount = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0}
	for y in p.split(' '):		#find segment 6
		for z in list(y):
			scount[z] += 1
		for z in segments:
			if scount[z] == 9:
				s6 = z
	for y in one:				#find segment 3
		if y != s6:
			s3 = y
	print(s3)
	for y in p.split(' '):		#segments in 4
		if len(y) == 4:
			four = list(y)
	for y in p.split(' '):		#find segment 2
		if len(y) == 5:
			u = y
			c = 0
			n = []
			for z in segments:
				if z not in u and z in four:
					n.append(z)
					c += 1
			if c == 2:
				for z in n:
					if z != s6:
						s2 = z
	print(s2)
	for y in p.split(' '):		#segments in 2
		if len(y) == 5 and s6 not in list(y):
			two = list(y)
	for y in p.split(' '):		#find segment 5
		if len(y) == 6:
			for z in list(y):
				if z not in four:
					s5 = z
	for y in p.split(' '):		#segments in 6
		if len(y) == 6 and s3 not in list(y):
			six = list(y)
	for y in p.split(' '):		#find segment 4
		if len(y) == 6 and s3 in list(y) and s5 in list(y):
			zero = list(y)
			for z in segments:
				if z not in zero:
					s4 = z
	for y in segments:			#find segment 7
		if y not in [s1,s2,s3,s4,s5,s6]:
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
		elif len(y.strip()) == 6 and s3 not in list(y.strip()):
			numbers.append(6)
		elif len(y.strip()) == 3:
			numbers.append(7)
		elif len(y.strip()) == 7:
			numbers.append(8)
		elif len(y.strip()) == 6 and s5 not in list(y.strip()):
			numbers.append(9)
	c += numbers[0] ** 3 + numbers[1] ** 2 + numbers[2] ** 1 + numbers[3]
print(c)