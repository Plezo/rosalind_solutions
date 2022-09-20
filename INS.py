def solve(ds):
    n = int(ds[0])
    arr = [int(i) for i in ds[1].split(' ')]

    swaps = 0

    for i in range(1, n, 1):
        temp = i
        while temp >= 1 and arr[temp] < arr[temp-1]:
            arr[temp-1], arr[temp] = arr[temp], arr[temp-1]
            temp -= 1
            swaps += 1

    print(swaps)

if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)