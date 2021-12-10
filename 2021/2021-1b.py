f = open('2021-1.txt')
f = f.readlines()
c = 0
def r(a):
	return int(a.removesuffix('\n'))
for i, d in enumerate(f[3:]):
	if r(f[i]) + r(f[i+1]) + r(f[i+2]) < r(f[i+1]) + r(f[i+2]) + r(d):
		c += 1
print(c)