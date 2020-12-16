d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
	legs = d[animal]
	print('A % has %d legs' % (animal, legs))