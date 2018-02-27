def match_len(s1, s2):
    """Returns length of the longest suffix of s1 matching prefix of s2"""
    n = min(len(s1), len(s2))
    for k in range(n, n//2, -1):
        if s1[len(s1)-k:] == s2[:k]:
            return k
    return 0


def restore_superstring(seqs, next, match):
    i = 0
    while i in next:
        i+= 1
    superstring = seqs[i]
    while next[i] != -1:
        superstring += seqs[next[i]][match[i]:]
        i = next[i]
    return superstring


def genome_assembly(seqs):
    next = [-1 for _ in range(len(seqs))]
    match = [-1 for _ in range(len(seqs))]
    for i in range(len(seqs)-1):
        for j in range(i+1, len(seqs)):
            k1 = match_len(seqs[i], seqs[j])
            if k1 > 0:
                next[i] = j
                match[i] = k1
            k2 = match_len(seqs[j], seqs[i])
            if k2 > 0:
                next[j] = i
                match[j] = k2
    return restore_superstring(seqs, next, match)


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
    out.write(genome_assembly(seqs))
