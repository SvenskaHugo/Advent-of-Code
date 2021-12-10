f = open('2020-4.txt')
f = f.readlines()
f = ''.join(f)
f = f.split('\n\n')
fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
for i,s in enumerate(f):
	f[i] = s.replace('\n', ' ')
c = 0
for x in f:
	c += 1
	for y in fields:
		if y not in x:
			c -= 1
			break
print(c)