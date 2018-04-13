import Queue


def infer_peptide_from_full_spectrum(ions, mass_table):
    n = len(ions)
    ions.sort()

    #construct graph
    diffs_graph = [{} for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            diff = ions[j] - ions[i]
            if diff < 200:
                for amino_acid, mass in mass_table.items():
                    if abs(mass - diff) < 0.01:
                        diffs_graph[i][j] = amino_acid

    # find possible peptides
    peptides = ["" for _ in range(n)]
    q = Queue.Queue()
    q.put(0)
    while not q.empty():
        u = q.get()
        for v, amino_acid in diffs_graph[u].items():
            peptides[v] = peptides[u] + amino_acid
            q.put(v)

    # get the longest peptide
    res = ""
    for peptide in peptides:
        if len(peptide) > len(res):
            res = peptide
    return res




with open("MonoisotopicMassTable.txt") as f:
    mass_table = {}
    for line in f.readlines():
        amino_acid, mass = line.strip().split()
        mass_table[amino_acid] = float(mass)

with open("input.txt", 'r') as f:
    spectrum = []
    for line in f.readlines():
        spectrum.append(float(line.strip()))

with open("output.txt", 'w') as out:
    out.write(infer_peptide_from_full_spectrum(spectrum, mass_table))