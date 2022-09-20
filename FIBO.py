def solve(ds):
    n = int(ds[0])
    a = 1
    b = 1

    for _ in range(2, n, 1):
        a, b = b, b + a
    
    print(b)

if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)