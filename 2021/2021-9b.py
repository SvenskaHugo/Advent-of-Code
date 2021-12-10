import time
f = open('2021-9.txt')
f = f.readlines()
r = 0
for x in range(len(f)):
	f[x] = list(f[x].strip())
def neighbors(f,x,y):
	s = 0
	if f[x][y] in ['9','#']:
		return s
	f[x][y] = '#'
	if  x < len(f) - 1:
		s += neighbors(f,x+1,y)
	if  y < len(f[x]) - 1:
		s += neighbors(f,x,y+1)
	if  x > 0:
		s += neighbors(f,x-1,y)
	if  y > 0:
		s += neighbors(f,x,y-1)
	return s+1
largest = [0,0,0]
for x,a in enumerate(f):
	for y,b in enumerate(a):
		size = neighbors(f,x,y)
		largest.sort()
		if size > largest[0]:
			largest[0] = size
c = 1
for x in largest:
	c *= x
print(c)