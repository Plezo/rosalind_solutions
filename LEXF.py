import itertools

def solve(ds):
    alphabet = [i for i in ds[0].split(' ')]
    n = int(ds[1])

    perm = list(itertools.product(alphabet, repeat=n))

    for i in perm:
        for ch in i:
            print(ch, end='')
        print()


if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)