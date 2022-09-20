def bins(arr, target):
    i, j = 0, len(arr)-1

    while (i <= j):

        mid = i + (j-i)//2

        if arr[mid] > target:
            j = mid-1
        elif arr[mid] < target:
            i = mid+1
        else:
            return mid+1

    return -1

def solve(ds):
    n, m = int(ds[0]), int(ds[1])
    arr, targets = [int(i) for i in ds[2].split(' ')], [int(i) for i in ds[3].split(' ')]

    for t in targets:
        print(bins(arr, t), end=' ')

if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)