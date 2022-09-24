from math import factorial

def solve(ds):
    n, k = [int(i) for i in ds[0].split(' ')]
    
    print(int((factorial(n) / (factorial(n-k))) % 1000000))

if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)