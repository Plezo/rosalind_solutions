def solve(ds):
    ds = [int(i) for i in ds[0].split(' ')]

    dct = {
        0: 1,
        1: 1,
        2: 1,
        3: 0.75,
        4: 0.5,
        5: 0
    }

    res = 0
    
    # num couples * 2 offstring * P(getting a dominant)
    for i in range(len(ds)):
        if ds[i] > 0:
            res += ds[i] * 2 * dct[i]
    
    print(res)

if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)