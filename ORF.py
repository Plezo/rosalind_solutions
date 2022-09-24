# Needs revision!!

import re

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

def dnaToProtein(dna):
    codon_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

    return ''.join([codon_table.get(dna[i:i+3], 'None') for i in range(0, len(dna), 3)])

def getCompliment(dna):
    dct = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A',
    }

    return ''.join([dct[ch] for ch in dna][::-1])

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