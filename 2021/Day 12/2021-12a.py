f = open('2021-12.txt')
f = f.readlines()
pths = {}
for x in f:
	for y in x.split('-'):
		if y not in list(pths.keys()):
			pths[y.strip()] = []
for x,a in enumerate(f):
	b = a.strip()
	f[x] = b.split('-')
for x in f:
	pths[x[0]] = []
	pths[x[1]] = []
for x in f:
	pths[x[0]].append(x[1])
	pths[x[1]].append(x[0])
c = 0
def visit(rm,pth):
	global c
	if rm == 'end':
		c += 1
		print('end')
		return
	for x in pths[rm]:
		if rm.isupper() or rm not in pth:
			t = pth.copy()
			t.append(rm)
			visit(x,t)
visit('start',[])
print(c)