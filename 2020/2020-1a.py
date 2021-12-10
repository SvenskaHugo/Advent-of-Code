f = open('2020-1.txt')
f = f.readlines()
for x in f:
	i = int(x.removesuffix('\n'))
	print(i)
	print(2020-i)
	if f'{2020 - i}\n' in f:
		print((2020 - i) * i)
		break