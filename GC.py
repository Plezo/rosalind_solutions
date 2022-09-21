def solve(ds):

	# Format string into dct, ID is key, dna is value
	dct = {}
	k = ''
	for i in range(len(ds)):
		if ds[i][0] == '>':
			k = ds[i][1:]
		else:
			dct[k] = dct.get(k, '') + ds[i]

	maxGC = ('', 0)
	for ID, dna in dct.items():
		gcCount = 100 * (dna.count('C') + dna.count('G')) / len(dna)
		if maxGC[1] < gcCount:
			maxGC = (ID, gcCount)

	print(maxGC[0])
	print(maxGC[1])

if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)