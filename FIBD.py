def solve(ds):
    n, m = [int(i) for i in ds[0].split(' ')]

    fib = [1, 1]
    for i in range(2, n, 1):

        if 0 <= i - (m+1) < len(fib): # takes into account dying rabbits
            temp = fib[i-2] + fib[i-1] - fib[i - (m+1)]
        elif i == m: # first batch of dying rabbits
            temp = fib[i-2] + fib[i-1] - 1
        else: # before i == m
            temp = fib[i-2] + fib[i-1]
        
        fib.append(temp)
    
    print(fib[-1])

if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)