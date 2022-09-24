import itertools

def solve(ds):
    n = int(ds[0])

    nlist = [i for i in range(1, n+1, 1)]

    permutations = list(itertools.permutations(nlist))

    print(len(permutations))
    for tup in permutations:
        for i in tup:
            print(i, end=' ')
        print()

if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)