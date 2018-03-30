import math


def counting_disease_carriers(p):
    return 1 - ((1 - p)/(1 + math.sqrt(p))) ** 2


with open("input.txt", 'r') as f:
    probs = map(float, f.readline().strip().split())

with open("output.txt", 'w') as out:
    out.write(" ".join(map(str, (map(counting_disease_carriers, probs)))))