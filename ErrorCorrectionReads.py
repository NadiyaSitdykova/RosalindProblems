def complement_bp(bp):
    if bp == "A":
        return "T"
    if bp == "T":
        return "A"
    if bp == "C":
        return "G"
    if bp == "G":
        return "C"
    return ""


def reverse_complement(s):
    ss = ""
    for bp in s:
        ss += complement_bp(bp)
    return ss[::-1]


def singe_mismatch_position(s1, s2):
    mismatch_pos = -1
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if mismatch_pos != -1:
                return -1
            mismatch_pos = i
    return mismatch_pos


def divide_corrects_incorrects(reads):
    read_counts = {}
    for read in reads:
        rev_comp = reverse_complement(read)
        if read in read_counts:
            read_counts[read] += 1
        elif rev_comp in read_counts:
            read_counts[rev_comp] += 1
        else:
            read_counts[read] = 1

    correct, incorrect = [], []
    for read, count in read_counts.items():
        if count > 1:
            correct.append(read)
        else:
            incorrect.append(read)

    return correct, incorrect


def corrected_read(corrects, incorrect):
    for correct in corrects:
        if singe_mismatch_position(correct, incorrect) != -1:
            return correct
        if singe_mismatch_position(reverse_complement(correct), incorrect) != -1:
            return reverse_complement(correct)
    return ""


def error_correction(reads):
    corrects, incorrects = divide_corrects_incorrects(reads)
    corrections = []
    for incorrect in incorrects:
        corrections.append(incorrect + "->" + corrected_read(corrects, incorrect) + "\n")
    return corrections


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
    reads = parse_fasta(f.readlines())

with open("output.txt", 'w') as out:
    out.writelines(error_correction(reads))