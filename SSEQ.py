from utils import *

def solve(ds):
    s = ds[0]
    t = list(ds[1])

    i = 0
    while i < len(s) and len(t) != 0:
        if s[i] == t[0]:
            t.pop(0)
            print(i+1, end=' ')
        i += 1

if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]

    ds = list(getFASTADict(ds).values())

    solve(ds)