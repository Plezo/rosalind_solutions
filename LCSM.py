# Naive approach

from utils import *

def solve(ds):
    
    sets = []

    for dna in ds:
        subs = set()
        for i in range(len(dna)):
            for j in range(i, len(dna)):
                subs.add(dna[i:j+1])
        sets.append(subs)

    intersect = sets[0].intersection(*sets)
    res = max(intersect, key=lambda x: len(x))

    print(res)

if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]

    ds = list(getFASTADict(ds).values())

    solve(ds)