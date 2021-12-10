f = open('2021-9.txt')
f = f.readlines()
r = 0
for x,a in enumerate(f):
	for y,b in enumerate(list(a.strip())):
		lowest = True
		try:
			if int(f[x-1][y]) <= int(b):
				lowest = False
		except:
			pass
		try:
			if int(f[x][y-1]) <= int(b):
				lowest = False
		except:
			pass
		try:
			if int(f[x][y+1]) <= int(b):
				lowest = False
		except:
			pass
		try:
			if int(f[x+1][y]) <= int(b):
				lowest = False
		except:
			pass
		if lowest:
			print(x,y,b)
			r += int(b) + 1
print(r)