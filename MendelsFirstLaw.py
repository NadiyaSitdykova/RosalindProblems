def recessive_homozygous_2(n, total):
    if (total > 1):
        return n/total * (n-1)/(total-1)
    return 0

def recessive_homozygous_heterozygous(n, m, total):
    if (total > 1):
        return (n/total * m/(total-1) + m/total * n/(total-1)) * 0.5
    return 0

def heterozygous_2(m, total):
    if (total > 1):
        return m/total * (m-1)/(total-1) * 0.25
    return 0


with open("input.txt", 'r') as file:
    k, m, n = map(float, file.readline().split())

t = k + m + n

with open("output.txt", 'w') as out:
    out.write(str(1 - recessive_homozygous_2(n, t) - recessive_homozygous_heterozygous(n, m, t) - heterozygous_2(m, t)))

