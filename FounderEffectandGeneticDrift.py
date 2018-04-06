import math


def binom_coeff(n, k):
    k = min(k, n-k)
    if k < 0 or k > n: return  0
    if k == 0: return 1
    numerator = reduce(lambda x,y: x*y, xrange(n, n-k, -1))
    denomerator = reduce(lambda x,y: x*y, xrange(1, k+1))
    return numerator//denomerator


def exact_prob(n, k, p):
    return binom_coeff(n, k) * p ** k * (1 - p) ** (n - k)


def wright_fisher_model(n, m, g, k):
    p = [0.0 for _ in range(2*n+1)]
    p[m] = 1.0
    for _ in range(0, g):
        pp = [0.0 for _ in range(2*n+1)]
        for i in range(2*n+1):
            pp[i] += sum([p[j] * exact_prob(2*n, i, float(j)/(2*n)) for j in range(2*n+1)])
        p = pp
    res = sum(p[:(2*n-k+1)])
    return res


def founder_effect(N, m, A):
    k = len(A)
    B = [[0 for _ in range(k)] for _ in range(m)]
    for gene_number in range(k):
        p = [0.0 for _ in range(2 * N + 1)]
        p[A[gene_number]] = 1.0
        for generation_number in range(m):
            pp = [0.0 for _ in range(2 * N + 1)]
            for i in range(2 * N + 1):
                pp[i] += sum([p[j] * exact_prob(2 * N, i, float(j) / (2 * N)) for j in range(2 * N + 1)])
            p = pp
            B[generation_number][gene_number] = math.log10(p[0])
    return B


with open("input.txt", 'r') as f:
    N, m = map(int, f.readline().strip().split())
    A = map(int, f.readline().strip().split())

with open("output.txt", 'w') as out:
    for row in founder_effect(N, m, A):
        out.write(" ".join(map(str, row)) + "\n")