f = open('2020-4.txt')
f = f.readlines()
f = ''.join(f)
f = f.split('\n\n')
fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
for i,s in enumerate(f):
	f[i] = s.replace('\n', ' ')
c = 0
for x in f:
	if len(x) < 7:
		continue
	for y in x.split(' '):
		valid = True
		if y[0:3] == 'byr' and not 1920 <= int(y[4:]) <= 2002:
			valid = False
		elif y[0:3] == 'iyr' and not 2010 <= int(y[4:]) <= 2020:
			valid = False
		elif y[0:3] == 'eyr' and not 2020 <= int(y[4:]) <= 2030:
			valid = False
		elif y[0:3] == 'hgt':
			if y[-2:] == 'cm' and not 150 <= int(y[4:-2]) <= 193:
				valid = False
			elif y[-2:] == 'in' and not 59 <= int(y[4:-2]) <= 76:
				valid = False
			else:
				print(f'split seems to be wrong. {y[-2:]}')
		elif y[0:3] == 'hcl':
			if len(y[5:]) != 6
				valid = False
			else:
				for x in y[5:]:
					if x not in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']:
						valid = False
						break
		elif y[0:3] == 'ecl':
			if y[4:] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
				valid = False
		elif y[0:3] == 'pid':
			if y[]
print(c)	for x in y[3:]