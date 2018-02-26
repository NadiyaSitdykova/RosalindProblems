import operator


def retrace_subseq(d, p, compare):
    i = d.index(max(d))
    subseq = [p[i]]
    for j in range(i-1, -1, -1):
        if compare(p[i], p[j]) and d[j] == d[i] - 1:
            i = j
            subseq.append(p[i])
    return reversed(subseq)


def longest_subseq(n, p, compare):
    d = [1]
    for i in range(1, n):
        max_len = 0
        for j in range(i):
            if compare(p[i], p[j]):
                max_len = max(max_len, d[j]+1)
        d.append(max_len)
    return retrace_subseq(d, p, compare)


with open("input.txt", 'r') as file:
    n = int(file.readline())
    p = map(int, file.readline().split())

with open("output.txt", 'w') as out:
    inc_subseq = longest_subseq(n, p, operator.gt)
    dec_subseq = longest_subseq(n, p, operator.lt)
    out.write(" ".join(map(str, inc_subseq)) + "\n")
    out.write(" ".join(map(str, dec_subseq)))