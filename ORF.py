# Needs revision!!

from utils import *

def solve(dna):

    # Store all places we have starts
    starts = []
    for i in range(len(dna)):
        if dnaToProtein(dna[i:i+3]) == 'M':
            starts.append(i)

    proteins = []

    for i in starts:
        res = ''
        stop = False

        # Print strings from every index that represents M
        for j in range(i, len(dna), 3):
            protein = dnaToProtein(dna[j:j+3])

            if protein == 'None':
                break

            if protein == '_':
                stop = True
                break
            res += protein

        if stop:
            proteins.append(res)
    return proteins

if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]

    # Compress all lines of dna to one long dna string
    dct = {}
    k = ''
    for i in range(len(ds)):
        if ds[i][0] == '>':
            k = ds[i][1:]
        else:
            dct[k] = dct.get(k, '') + ds[i]

    ds = list(dct.values())[0]

    # Need to check all substrings for dna and its compliment
    ans = set(solve(ds) + solve(getCompliment(ds)))

    for i in ans:
        print(i)