f = open('2021-13.txt')
f = f.readlines()
f = ''.join(f)
dots = f.split('\n\n')[0]
folds = f.split('\n\n')[1]
dots = dots.split('\n')
folds = folds.split('\n')
for i,x in enumerate(dots):
	dots[i] = [int(x.split(',')[0]),int(x.split(',')[1])]
for i,x in enumerate(folds):
	t = x.split(' ')[2]
	folds[i] = [t.split('=')[0],int(t.split('=')[1])]
for f in folds:
	dtemp = []
	for d in dots:
		if f[0] == 'y':
			new = [d[0],abs(d[1]-f[1])-1]
			if new not in dtemp:
				dtemp.append(new)
		elif f[0] == 'x':
			new = [abs(d[0]-f[1])-1,d[1]]
			if new not in dtemp:
				dtemp.append(new)
	dots = dtemp.copy()
paper = []
for x in range(40):
	paper.append([])
	for y in range(10):
		paper[x].append(' ')
for x in dots:
	paper[x[0]][x[1]] = '#'
paper.reverse()
print(paper)