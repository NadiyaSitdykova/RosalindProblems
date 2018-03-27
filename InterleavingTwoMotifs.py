def match(bp1, bp2):
    return int(bp1 == bp2)


def least_common_subseq(s1, s2):
    # compute score matrix d
    d = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            d[i][j] = max(d[i-1][j],
                          d[i][j-1],
                          d[i-1][j-1] + match(s1[i-1], s2[j-1]))

    # retrace least common subseq
    rev_lcs = ""
    i, j = len(s1), len(s2)
    while i > 0 and j > 0:
        if d[i][j] == d[i-1][j-1] + match(s1[i-1], s2[j-1]):
            i -= 1
            j -= 1
            if s1[i] == s2[j]:
                rev_lcs += s1[i]
        elif d[i][j] == d[i-1][j]:
            i -= 1
        elif d[i][j] == d[i][j-1]:
            j -= 1
    return rev_lcs[::-1]


def least_common_superseq(s1, s2):
    lcs = least_common_subseq(s1, s2)
    res = ""
    n, m = len(s1), len(s2)
    i, j = 0, 0
    for k in range(len(lcs)):
        while i < n and s1[i] != lcs[k]:
            res += s1[i]
            i += 1
        while j < m and s2[j] != lcs[k]:
            res += s2[j]
            j += 1
        res += lcs[k]
        i += 1
        j += 1
    while i < n:
        res += s1[i]
        i += 1
    while j < m:
        res += s2[j]
        j += 1
    return res


with open("input.txt", 'r') as f:
    s1 = f.readline().strip()
    s2 = f.readline().strip()

with open("output.txt", 'w') as out:
    out.write(least_common_superseq(s1, s2))