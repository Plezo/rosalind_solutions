def solve(ds):

    dct = {
    'A': 0,
    'C': 0,
    'G': 0,
    'T': 0
    }

    for ch in ds[0]:
        if ch in dct:
            dct[ch] += 1

    for i in dct.items():
        print(i[1], end=' ')


if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]

    res = str(solve(ds))

    # print(res)

    with open('result.txt', 'w') as f:
        f.write(res)