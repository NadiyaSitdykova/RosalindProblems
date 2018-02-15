def calculate_offspring(coeff):
    return 2 * sum(coeff[:3]) + 1.5 * coeff[3] + coeff[4]

with open("input.txt", 'r') as file:
    coeff = map(int, file.readline().split())

with open("output.txt", 'w') as out:
    out.write(str(calculate_offspring(coeff)))