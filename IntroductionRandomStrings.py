import math


def compute_log_prob(nucleotide, GC_probability):
    if nucleotide == 'C' or nucleotide == 'G':
        return math.log(GC_probability/2, 10)
    elif nucleotide == 'A' or nucleotide == 'T':
        return math.log((1-GC_probability)/2, 10)
    return 0


with open("input.txt", 'r') as file:
    s = file.readline().strip()
    GC_content_values = list(map(float, file.readline().strip().split()))

with open("output.txt", 'w') as out:
    for GC in GC_content_values:
        total_probability = 0
        for c in s:
            total_probability += compute_log_prob(c, GC)
        out.write(str(total_probability) + " ")