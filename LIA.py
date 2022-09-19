from scipy.special import comb

def solve(ds):
    k, N = [int(i) for i in ds[0].split(' ')]

    res = 0

    # Binomial Distribution
    # nCx * p^x * q^(n-x)
    for n in range(N):
        res += comb(2**k, n) * (0.25**n) * (0.75**(2**k-n))

    print(1 - res)

if __name__ == '__main__':
    f = open('ds.txt', 'r')
    ds = [line.strip() for line in f]
    solve(ds)