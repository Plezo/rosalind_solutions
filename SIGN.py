import math
import itertools

def solve(ds):
	n = int(ds[0])
	arr = [i for i in range(1, n+1)]
	permutations = list(itertools.permutations(arr, r=n))
	res = []
	
	for p in permutations:
		temp = itertools.product([-1, 1], repeat=len(arr))
		for i in temp:
			res.append([x*y for x, y in zip(p, i)])

	print(len(res))
	for p in res:
		print(*p, sep=' ')


if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)