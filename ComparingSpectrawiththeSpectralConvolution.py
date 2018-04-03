def compare_spectra(spectrum1, spectrum2):
    #compute minkowski_differense and shared_mass of spectrum1 and spectrum2
    minkowski_difference = {}
    for m1 in spectrum1:
        for m2 in spectrum2:
            diff = round(m1 - m2, 10)
            if diff not in minkowski_difference:
                minkowski_difference[diff] = 0
            minkowski_difference[diff] += 1

    #find largest_multiplitcity and max_peak
    largest_multiplitcity = 0
    max_shared_peaks = 0
    for shift, multiplitcity in minkowski_difference.items():
        if multiplitcity > largest_multiplitcity:
            largest_multiplitcity = multiplitcity
            maximizing_shift = shift

    return largest_multiplitcity, maximizing_shift


with open("input.txt", 'r') as f:
    sp1 = map(float, f.readline().strip().split())
    sp2 = map(float, f.readline().strip().split())

with open("output.txt", 'w') as out:
    out.write("\n".join(map(str, compare_spectra(sp1, sp2))))