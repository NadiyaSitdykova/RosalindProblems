def match(bp1, bp2):
    return int(bp1 == bp2)


def retrace_motif(d, s1, s2):
    rev_motif = ""
    i, j = len(s1), len(s2)
    while i > 0 and j > 0:
        if d[i][j] == d[i-1][j-1] + match(s1[i-1], s2[j-1]):
            i -= 1
            j -= 1
            if s1[i] == s2[j]:
                rev_motif += s1[i]
        elif d[i][j] == d[i-1][j]:
            i -= 1
        elif d[i][j] == d[i][j-1]:
            j -= 1
    return rev_motif[::-1]


def shared_splicing_motif(s1, s2):
    d = [[0 for _ in range(len(s2)+1)] for _ in range(len(s2)+1)]
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            d[i][j] = max(d[i-1][j],
                          d[i][j-1],
                          d[i-1][j-1] + match(s1[i-1], s2[j-1]))
    print(d[len(s1)][len(s2)])
    motif = retrace_motif(d, s1, s2)
    return motif


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
    out.write(shared_splicing_motif(s1, s2))