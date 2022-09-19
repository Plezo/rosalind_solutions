def solve(ds):
    for ch in ds[0]:
        if ch == 'T':
            print('U', end='')
        else:
            print(ch, end='')


if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)