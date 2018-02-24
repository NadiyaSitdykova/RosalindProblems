def find_spliced_motif(s, t):
    indices = []
    i = 0
    for j in range(len(t)):
        while i < len(s) and s[i] != t[j]:
            i += 1
        if i == len(s):
            return []
        indices.append(i + 1)
        i += 1
    return indices

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
    out.write(" ".join(map(str, find_spliced_motif(seqs[0], seqs[1]))))