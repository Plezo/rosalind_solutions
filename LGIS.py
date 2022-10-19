def solve(ds):
    arr = [int(i) for i in ds[1].split(' ')]

    asc = []
    desc = []

    # Ascending
    for i in range(len(arr)):
        temp = []
        for j in range(i):
            if asc[j][-1] < arr[i]:
                temp.append(asc[j])
        asc.append(max(temp or [[]], key=len) + [arr[i]])

    # Descending
    for i in range(len(arr)):
        temp = []
        for j in range(i):
            if desc[j][-1] > arr[i]:
                temp.append(desc[j])
        desc.append(max(temp or [[]], key=len) + [arr[i]])
    
    res = max(asc, key=len)

    for i in res:
        print(i, end=' ')

    print()

    res = max(desc, key=len)

    for i in res:
        print(i, end=' ')

if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)