def rev_comp(s):
    comp = ""
    for c in s:
        if c == "A":
            comp += "T"
        if c == "T":
            comp += "A"
        if c == "C":
            comp += "G"
        if c == "G":
            comp += "C"
    return comp[::-1]


def construct_de_bruin_graph(kmers):
    g = {}
    for kmer in kmers:
        u = kmer[:-1]
        v = kmer[1:]
        if u not in g:
            g[u] = set()
        g[u].add(v)

    return g


with open("input.txt", 'r') as f:
    kmers = []
    for line in f.readlines():
        read = line.strip()
        kmers.append(read)
        kmers.append(rev_comp(read))


de_bruin_graph = construct_de_bruin_graph(kmers)

with open("output.txt", 'w') as out:
    for u, vs in de_bruin_graph.items():
        for v in vs:
            out.write("(" + u + ", " + v + ")\n")
