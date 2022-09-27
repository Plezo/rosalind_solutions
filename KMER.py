import itertools
from utils import *

def solve(ds):

	dct = dict()

	# Store all possible combinations
	for kmer in [''.join(i) for i in itertools.product('ATGC', repeat=4)]:
		dct[kmer] = 0

	# Populate dict with existing ones in str
	for i in range(len(ds)-3):
		dct[ds[i:i+4]] += 1

	# Sort lexicographically
	srt = sorted(dct.keys())

	for i in srt:
		print(dct[i], end=' ')


if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]

    ds = getFASTADict(ds)

    solve(list(ds.values())[0])