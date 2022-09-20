def solve(ds):
    s = ds[0]
    t = ds[1]

    counter = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            counter += 1
    
    print(counter)

if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)