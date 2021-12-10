f = open('strs.txt')
f = f.readlines()
vowels = ['a','e','i','o','u']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
t = 0
for x in f:
	c = 0
	for y in alphabet:
		for z in alphabet:
			if x.count(f'{y}{z}') == 2:
				c = 1
	v = 0
	for y in range(len(x) - 2):
		if x[y] == x[y+2]:
			v = 1
	if v and c:
		t += 1
		print(f'{x} is nice, t is now {t}')
print(t)