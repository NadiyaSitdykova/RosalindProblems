def all_kmers(k):
    if k == 0:
        return [""]
    res = []
    for kmer in all_kmers(k-1):
        res.append(kmer + "A")
        res.append(kmer + "C")
        res.append(kmer + "G")
        res.append(kmer + "T")
    return res


def kmer_composition(s, k):
    kmer_counter = {}
    for kmer in all_kmers(k):
        kmer_counter[kmer] = 0

    for i in range(len(s)-k+1):
        kmer = s[i:i+k]
        kmer_counter[kmer] += 1
    return kmer_counter


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
    print(s)

with open("output.txt", 'w') as out:
    composition = kmer_composition(s, 4)
    for kmer, count in sorted(composition.items()):
        print(kmer)
        out.write(str(count) + " ")
