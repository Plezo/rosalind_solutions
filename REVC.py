def solve(ds):
    dct = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A',
    }

    for i in range(len(ds[0])-1, -1, -1):
        print(dct[ds[0][i]], end='')


if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)