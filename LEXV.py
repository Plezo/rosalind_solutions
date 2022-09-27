import itertools

def solve(ds):
    alphabet = [i for i in ds[0].split(' ')]
    n = int(ds[1])

    # Create all permutations 1...n
    perms = []
    for i in range(1, n+1, 1):
        for p in list(itertools.product(alphabet, repeat=i)):
            res = ''
            for e in p:
                res += e
            perms.append(res)

    # Sort lexicographically based on where it is in the alphabet
    srt = sorted(perms, key=lambda x: [alphabet.index(ch) for ch in x])

    # Writing to file since output too big for terminal
    with open('result.txt', 'w') as file:
        for i in srt:
            file.write(i + '\n')


if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)