def solve(ds):
    s = ds[0]
    t = ds[1]

    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            print(i+1, end=' ')

if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)