f = open('2020-2.txt')
f = f.readlines()
v = 0
for x in f:
	l = x.split(' ')
	r = l[0]
	s = l[2]
	k = l[1][0]
	a = int(r.split('-')[0])
	b = int(r.split('-')[1])
	if a <= s.count(k) <= b:
		v += 1
print(v)