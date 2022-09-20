def solve(ds):
    k, n = [int(i) for i in ds[0].split(' ')]
    arrs = [[int(j) for j in i.split(' ')] for i in ds[1:]]

    res = []

    for arr in arrs:
        dct = {}
        for i in range(len(arr)):
            dct[arr[i]] = dct.get(arr[i], 0) + 1
            if dct[arr[i]] > n / 2:
                print(arr[i], end=' ')
                break
            elif i == len(arr)-1:
                print(-1, end=' ')


if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)