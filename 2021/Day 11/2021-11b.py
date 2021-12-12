f = open('2021-11.txt')
f = f.readlines()
for x,a in enumerate(f):
	f[x] = list(a.strip())
c = 0
def inc(x,y,f):
	f = f.copy()
	try:
		if f[x][y] == '9':
			f[x][y] = '#'
			for a in [-1,0,1]:
				for b in [-1,0,1]:
					if 0<=x+a<len(f) and 0<=y+b<=len(f[x]):
						inc(x+a,y+b,f)
		elif f[x][y] != '#':
			f[x][y] = str(int(f[x][y])+1)
	except:
		pass
i = 0
while True:
	i += 1
	for x,a in enumerate(f):
		for y,b in enumerate(a):
			inc(x,y,f)
	sync = True
	for x,a in enumerate(f):
		for y,b in enumerate(a):
			if b == '#':
				f[x][y] = '0'
				c += 1
			else:
				sync = False
	if sync:
		break
print(i)