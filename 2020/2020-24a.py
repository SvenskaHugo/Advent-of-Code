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
print(len(g))