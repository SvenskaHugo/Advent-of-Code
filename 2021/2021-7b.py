f = open('2021-7.txt')
f = f.readlines()
f = f[0].split(',')
for i,x in enumerate(f):
	f[i] = int(x)
def calcfuel(f,l):
	c = 0
	for x in f:
		c += sum(range(int(abs(l-x))+1))
	return c
def testneighbors(f,l):
	a, b, c = calcfuel(f,l-1), calcfuel(f,l), calcfuel(f,l+1)
	if a < b < c:
		return 1
	elif a > b < c:
		return 0
	elif a > b > c:
		return -1
running = True
x = len(f)/2
i = x
while running:
	i /= 2
	i = round(i)
	if testneighbors(f,x) == 0:
		running = False
	elif testneighbors(f,x) == 1:
		x -= i
	elif testneighbors(f,x) == -1:
		x += i
print(calcfuel(f,x))