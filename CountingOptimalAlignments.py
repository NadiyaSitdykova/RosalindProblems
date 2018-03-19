def match(c1, c2):
    return int(c1 != c2)


def count_optimal_alignments(s1, s2):
    n, m = len(s1), len(s2)
    d = [[0 for _ in range(m+1)] for _ in range(n+1)]
    count = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        d[i][0] = i
        count[i][0] = 1
    for j in range(m+1):
        d[0][j] = j
        count[0][j] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            d[i][j] = min(d[i-1][j-1] + match(s1[i-1], s2[j-1]),
                          d[i-1][j] + 1,
                          d[i][j-1] + 1)
            if d[i][j] == d[i-1][j-1] + match(s1[i-1], s2[j-1]):
                count[i][j] += count[i-1][j-1]
            if d[i][j] == d[i-1][j] + 1:
                count[i][j] += count[i-1][j]
            if d[i][j] == d[i][j-1] + 1:
                count[i][j] += count[i][j-1]
    return count[n][m]


def parse_fasta(lines):
    seqs = []
    cur_seq = ""
    for line in lines[1:]:
        if line[0] == ">":
            seqs.append(cur_seq)
            cur_seq = ""
        else:
            cur_seq += line.strip()
    seqs.append(cur_seq)
    return seqs


with open("input.txt", 'r') as f:
    s1, s2 = parse_fasta(f.readlines())

with open("output.txt", 'w') as out:
    out.write(str(count_optimal_alignments(s1, s2) % 134217727))