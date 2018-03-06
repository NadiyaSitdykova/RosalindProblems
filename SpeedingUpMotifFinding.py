def failure_array(s):
    res = [0]
    j = 0
    for k in range(1, len(s)):
        while j > 0 and s[j] != s[k]:
            j = res[j-1]
        if s[j] == s[k]:
            j += 1
        res.append(j)
    return res


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
    out.write(" ".join(map(str, failure_array(s))))