from utils import *

def solve(ds):

    res = set()

    for k1, v1 in ds.items():
        for k2, v2 in ds.items():
            if v2 != v1 and v2[0:3] == v1[-3:]:
                res.add((k1, k2))

    for i in res:
        print(i[0], i[1])

if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]

    ds = getFASTADict(ds)

    solve(ds)