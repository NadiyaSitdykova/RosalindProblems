def infer_protein(spectrum, mass_table):
    protein = ""
    for i in range(len(spectrum)-1):
        cur_mass = spectrum[i+1] - spectrum[i]
        for amino_acid, mass in mass_table.items():
            if abs(mass-cur_mass) < (10**(-4)):
                protein += amino_acid
                break
    return protein


with open("MonoisotopicMassTable.txt") as f:
    mass_table = {}
    for line in f.readlines():
        amino_acid, mass = line.strip().split()
        mass_table[amino_acid] = float(mass)

with open("input.txt") as f:
    prefix_spectrum = map(float, f.readlines())


with open("output.txt", 'w') as out:
    out.write(infer_protein(prefix_spectrum, mass_table))