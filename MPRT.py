from utils import *
import re
import requests

# Sends request to get DNA from protein
def getDNA(protein):
    URL = f'http://www.uniprot.org/uniprot/{protein}.fasta'
    r = requests.get(url=URL)
    data = r.text
    return ''.join(data.split('\n')[1::])

def solve(ds):

    res = dict()
    
    for protein in ds:

        # Get first part of protein input
        try:
            working_protein = protein[0:protein.index('_')]
        except ValueError:
            working_protein = protein

        dna = getDNA(working_protein)

        # Finds positions of N-glycosylation motifs
        for match in re.finditer(r'N[^P](S|T)[^P]', dna):
            res[protein] = res.get(protein, []) + [match.start()+1]

    # Print results
    for k, v in res.items():
        print(k)
        for i in v:
            print(i, end=' ')
        print()



if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]

    solve(ds)