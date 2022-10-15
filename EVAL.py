import math

def solve(ds):
	n = int(ds[0])
	dna = ds[1]
	probs = [float(i) for i in ds[2].split(' ')]

	for p in probs:
		cg_prob = p / 2
		at_prob = (1 - p) / 2
		prob = 1.0

		for ch in dna:
			if ch in 'AT':
				prob *= at_prob
			else:
				prob *= cg_prob

		print(round(prob*(n-1), 3), end=' ')

if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)