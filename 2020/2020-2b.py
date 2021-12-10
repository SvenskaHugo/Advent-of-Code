f = open('2020-2.txt')
f = f.readlines()
v = 0
for x in f:
	l = x.split(' ')
	r = l[0].split('-')
	s = l[2]
	c = l[1][0]
	if ((s[int(r[0])-1] == c) + (s[int(r[1])-1] == c)) == 1:
		v += 1
print(v)