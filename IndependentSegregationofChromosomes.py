import math


def binom_coeff(n, k):
    k = min(k, n-k)
    if k < 0 or k > n: return  0
    if k == 0: return 1
    numerator = reduce(lambda x,y: x*y, xrange(n, n-k, -1))
    denomerator = reduce(lambda x,y: x*y, xrange(1, k+1))
    return numerator//denomerator


def exact_prob(n, k):
    return binom_coeff(n, k) * 0.5 ** n


def log_probabilities_at_least(n):
    probs = [0 for _ in range(2*n+1)]
    probs[2*n] = exact_prob(2*n, 2*n)
    for k in range(2*n-1, 0, -1):
        probs[k] = probs[k+1] + exact_prob(2*n, k)
    return map(lambda x: math.log(x, 10), probs[1:])


with open("input.txt", 'r') as f:
    n = int(f.readline())

with open("output.txt", 'w') as out:
    out.write(" ".join(map(str, log_probabilities_at_least(n))))