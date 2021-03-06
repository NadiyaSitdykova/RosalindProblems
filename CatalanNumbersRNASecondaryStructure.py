def is_pair(bp1, bp2):
    return (bp1=="A" and bp2=="U") \
           or (bp1=="U" and bp2=="A") \
           or (bp1=="C" and bp2=="G") \
           or (bp1=="G" and bp2=="C")


def non_crossing_perfect_matchings(s, d):
    if len(s) % 2 == 1:
        return 0
    if len(s) == 0:
        return 1
    if s not in d:
        d[s] = sum([int(is_pair(s[0], s[k]))
                    * non_crossing_perfect_matchings(s[1:k], d)
                    * non_crossing_perfect_matchings(s[k + 1:], d)
                    for k in range(1, len(s))])
    return d[s]


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
    s = parse_fasta(f.readlines())[0]

with open("output.txt", 'w') as out:
    out.write(str(non_crossing_perfect_matchings(s, {}) % 1000000))