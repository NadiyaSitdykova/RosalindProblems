def construct_de_bruin_graph(kmers):
    g = {}
    for kmer in kmers:
        u = kmer[:-1]
        v = kmer[1:]
        g[u] = v
    return g


def genome_assembly(reads):
    de_bruin_graph = construct_de_bruin_graph(reads)
    first_kmer = reads[0][:-1]
    u = de_bruin_graph[first_kmer]
    genome = u
    while u != first_kmer:
        v = de_bruin_graph[u]
        genome += v[-1]
        u = v
    return genome[:len(reads)]


with open("input.txt", 'r') as f:
    reads = []
    for line in f.readlines():
        reads.append(line.strip())

with open("output.txt", 'w') as out:
    out.write(genome_assembly(reads))