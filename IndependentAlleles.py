def binom_coeff(n, k):
    k = min(k, n-k)
    if k < 0 or k > n: return  0
    if k == 0: return 1
    numerator = reduce(lambda x,y: x*y, xrange(n, n-k, -1))
    denomerator = reduce(lambda x,y: x*y, xrange(1, k+1))
    return numerator//denomerator


def probability_of_exact_number(i, k):
    return binom_coeff(2**k, i) * (0.25)**i * (0.75)**(2**k - i)


def independent_alleles(k, n):
    return 1 - sum([probability_of_exact_number(i, k) for i in range(0, n)])


with open("input.txt", 'r') as file:
    k, n = map(int, file.readline().split())

with open("output.txt", 'w') as out:
    out.write(str(independent_alleles(k, n)))