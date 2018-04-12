def get_spectrum_of_protein(protein, mass_table):
    spectrum = [0, 0]
    for i in range(len(protein)):
        spectrum.append(spectrum[-2] + mass_table[protein[i]])
        spectrum.append(spectrum[-2] + mass_table[protein[len(protein) - i - 1]])
    return spectrum


def largest_multiplicity(spectrum1, spectrum2):
    #compute minkowski_differense and shared_mass of spectrum1 and spectrum2
    minkowski_difference = {}
    for m1 in spectrum1:
        for m2 in spectrum2:
            diff = round(m1 - m2, 10)
            if diff not in minkowski_difference:
                minkowski_difference[diff] = 0
            minkowski_difference[diff] += 1

    return max(minkowski_difference.values())


def match_spectrum_to_protein(proteins, spectrum, mass_table):
    overall_largest_multiplitcity = 0
    closest_protein = ""
    for protein in proteins:
        multiplicity = largest_multiplicity(get_spectrum_of_protein(protein, mass_table), spectrum)
        if multiplicity > overall_largest_multiplitcity:
            overall_largest_multiplitcity = multiplicity
            closest_protein = protein
    return overall_largest_multiplitcity, closest_protein


with open("MonoisotopicMassTable.txt") as f:
    mass_table = {}
    for line in f.readlines():
        amino_acid, mass = line.strip().split()
        mass_table[amino_acid] = float(mass)

with open("input.txt", 'r') as f:
    n = int(f.readline())
    proteins = []
    for _ in range(n):
        proteins.append(f.readline().strip())
    spectrum = []
    line = f.readline()
    while line:
        spectrum.append(float(line))
        line = f.readline()

with open("output.txt", 'w') as out:
    out.write("\n".join(map(str, match_spectrum_to_protein(proteins, spectrum, mass_table))))