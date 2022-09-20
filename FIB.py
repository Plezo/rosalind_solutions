def solve(ds):
    n, k = [int(i) for i in ds[0].split(' ')]
    a = 1
    b = 1

    for _ in range(3, n+1, 1):
        a, b = b, b + a*k
    
    print(b)

if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)