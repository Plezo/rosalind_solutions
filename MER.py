def solve(ds):
    n = int(ds[0])
    arr = [int(i) for i in ds[1].split(' ')]

    m = int(ds[2])
    arr2 = [int(i) for i in ds[3].split(' ')]

    i = j = 0

    res = []
    while i < n and j < m:
        if arr[i] < arr2[j]:
            res.append(arr[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    res += arr[i:] + arr2[j:]

    for a in res:
    	print(a, end=' ')

if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)