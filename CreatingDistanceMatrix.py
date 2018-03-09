def compute_distance(s1, s2):
    d = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            d += 1
    return float(d)/len(s1)


def create_distance_matrix(seqs):
    n = len(seqs)
    d = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            distance = compute_distance(seqs[i], seqs[j])
            d[i][j] = distance
            d[j][i] = distance
    return d


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


with open("input.txt", 'r') as file:
    seqs = parse_fasta(file.readlines())

with open("output.txt", 'w') as out:
    for row in create_distance_matrix(seqs):
        out.write(" ".join(map(str, row)) + "\n")