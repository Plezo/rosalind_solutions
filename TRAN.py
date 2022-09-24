from utils import *

def solve(ds):

    dct = {
        'A': 'G',
        'C': 'T',
        'G': 'A',
        'T': 'C',
    }
    
    s1 = list(ds.values())[0]
    s2 = list(ds.values())[1]

    transitions, transversions = 0, 0

    for i in range(len(s1)):
        if s1[i] == dct[s2[i]]:
            transitions += 1
        elif s1[i] != s2[i]:
            transversions += 1

    print(transitions / transversions)


if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]

    ds = getFASTADict(ds)

    solve(ds)