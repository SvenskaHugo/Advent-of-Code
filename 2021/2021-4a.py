f = open('2021-4.txt')
f = f.readlines()
n = f.pop(0)
del f[0]
f = ''.join(f)
f = f.split('\n\n')
boards = f

for x,y in enumerate(boards):
	boards[x] = y.split('\n')
for a in boards:
	for x,y in enumerate(a):
		a[x] = y.split(' ')
		for i,t in enumerate(a[x]):
			if t == '':
				del a[x][i]

def checkwin(a):
	for x in a:
		win = True
		for y in x:
			if type(y) != int:
				win = False
		if win:
			return True
	for x in range(5):
		win = True
		for y in a:
			if type(y[x]) != int:
				win = False
		if win:
			print('vertical victory')
			return True
	return False

def score(b):
	points = 0
	for x,y in enumerate(b):
		for a,c in enumerate(y):
			if type(c) != int:
				points += int(b[x][a])
	return points

def mark(b,n):
	for i,x in enumerate(b):
		for l,y in enumerate(x):
			if y == n:
				return [i,l]
	return False

n = n.split(',')

for t,x in enumerate(n):
	br = False
	for b,c in enumerate(boards):
		m = mark(c,x)
		if m:
			boards[b][m[0]][m[1]] = int(boards[b][m[0]][m[1]])
		if checkwin(boards[b]):
			points = int(x) * score(boards[b])
			print(boards[b])
			br = True
			break
	if br:
		print(t)
		break
print(points)