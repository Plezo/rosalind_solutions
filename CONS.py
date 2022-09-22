def solve(ds):

    # Format strings into dct, ID is key, dna is value
    dnas = {}
    k = ''
    for i in range(len(ds)):
        if ds[i][0] == '>':
            k = ds[i][1:]
        else:
            dnas[k] = dnas.get(k, '') + ds[i]

    # We only need values
    dnas = list(dnas.values())

    res = ""
    acgtCount = {
        'A': [0] * len(dnas[0]),
        'C': [0] * len(dnas[0]),
        'G': [0] * len(dnas[0]),
        'T': [0] * len(dnas[0])
    }

    # Populate dictionary (output needs it)
    for i in range(len(dnas)):
        for j in range(len(dnas[0])):
            acgtCount[dnas[i][j]][j] += 1

    # Output string
    for i in range(len(dnas[0])):
        maxACGT = ('', 0)
        for j in ['A', 'C', 'G', 'T']:
            if acgtCount[j][i] >= maxACGT[1]:
                maxACGT = (j, acgtCount[j][i])
        res += maxACGT[0]

    print(res)

    # Output dictionary
    for k, v in acgtCount.items():
        print(k + ':', end=' ')
        for i in v:
            print(i, end=' ')
        print()

if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)