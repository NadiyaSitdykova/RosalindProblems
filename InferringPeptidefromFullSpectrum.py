def infer_peptide_from_full_spectrum(spectrum, mass_table):
    ions = sorted(spectrum[1:])
    n = len(ions)

    #construct graph
    diffs_graph = [(None, None) for _ in range(n)]
    for i in range(n):
        for j in range(i):
            diff = ions[i] - ions[j]
            if diff < 200:
                for amino_acid, mass in mass_table.items():
                    if abs(mass - diff) < 0.000001:
                        diffs_graph[j] = (i, amino_acid)

    #follow path in graph
    u = 0
    peptide = ""
    while u < n-1:
        v, amino_acid = diffs_graph[u]
        u = v
        peptide += amino_acid

    return peptide[:0:-1]


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