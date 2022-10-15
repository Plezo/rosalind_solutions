import math

def solve(ds):
	N, x = [float(i) for i in ds[0].split(' ')]
	dna = ds[1]

	cg_prob = x / 2
	at_prob = (1 - x) / 2
	prob = 1.0

	for ch in dna:
		if ch in 'AT':
			prob *= at_prob
		else:
			prob *= cg_prob

	prob = 1-(1-prob)**N

	print(round(prob, 3), end=' ')

if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)