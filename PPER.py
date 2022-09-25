from utils import *

def solve(ds):
    dna = list(ds.values())[0]

    for i in range(len(dna)):
        sub = ''
        for j in range(12):

            if i + j >= len(dna):
                break

            sub += dna[i+j]

            if sub == getCompliment(sub):
                if 4 <= len(sub) <= 12:
                    print(i+1, j+1)



if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]

    ds = getFASTADict(ds)

    solve(ds)