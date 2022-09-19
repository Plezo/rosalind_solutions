def solve(ds):
    dct = {
        (0, 0): 1,      # k x k
        (0, 1): 1,      # k x m
        (0, 2): 1,      # k x n
        (1, 0): 1,      # m x k
        (1, 1): 0.75,   # m x m
        (1, 2): 0.5,    # m x n
        (2, 0): 1,      # n x k
        (2, 1): 0.5,    # n x m
        (2, 2): 0       # n x n
    }

    ds = [int(i) for i in ds[0].split(' ')]
    
    num_organisms = sum(ds)

    res = 0
    for i in range(3):

        base = ds[i] / num_organisms

        temp2 = ds[:]
        temp2[i] -= 1

        for j in range(3):

            inner = temp2[j] / (num_organisms-1)
            prob = dct[(i, j)]
            res += base * inner * prob

    return res

if __name__ == '__main__':
    f = open('rosalind_iprb.txt', 'r')
    ds = [line.strip() for line in f]

    res = str(solve(ds))

    print(res)

    with open('result.txt', 'w') as f:
        f.write(res)