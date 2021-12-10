f = open('2020-24.txt')
f = f.readlines()
g = []
m = {'e':(1,0),'w':(-1,0),'sw':(0,-1),'se':(1,-1),'nw':(-1,1),'ne':(0,1),}
for l in f:
	i = 0
	x = y = 0
	while i < len(l.strip()):
		if l[i] in ['e','w']:
			x += m[l[i]][0]
		else:
			x += m[l[i] + l[i+1]][0]
			y += m[l[i] + l[i+1]][1]
			i += 1
		i += 1
	if (x,y) in g:
		del g[g.index((x,y))]
	else:
		g.append((x,y))
for loop in range(100):
	b = []
	for x in g:
		for a in ['e','w','sw','se','nw','ne']:
			for i,c in enumerate(b):
				if c[0] == x[0] + m[a][0] and c[1] == x[1] + m[a][1]:
					b[i][2] += 1
				else:
					b.append([x[0],x[1],1])
	for i,c in enumerate(b):
		if (c[0],c[1]) in g and c[2] not in [1,2]:
			del g[g.index((c[0],c[1]))]
		elif c[2] == 2:
			g.append((c[0],c[1]))
