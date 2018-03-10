def count_subsets(n):
    return 2 ** n


with open("input.txt", 'r') as f:
    n = int(f.readline())

with open("output.txt", 'w') as out:
    out.write(str(count_subsets(n) % 1000000))
