f = open('2020-1.txt')
f = f.readlines()
for x in f:
	for y in f:
		for z in f:
			a = int(x.removesuffix('\n'))
			b = int(y.removesuffix('\n'))
			c = int(z.removesuffix('\n'))
			if a + b + c == 2020:
				print(a*b*c)