f = open('strs.txt')
f = f.readlines()
vowels = ['a','e','i','o','u']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
t = 0
for x in f:
	v = 0
	for y in vowels:
		v += x.count(y)
	c = 0
	for y in alphabet:
		c += x.count(f'{y}{y}')
	d = 0
	for y in ['ab','cd','pq','xy']:
		d += x.count(y)
	if v > 2 and c and not d:
		t += 1
		print(f'{x} is nice, t is now {t}')
print(t)