def count_subsets(n, m):
    factorials = [1, 1]
    for i in range(2, n+1):
        factorials.append(i * factorials[-1])
    return sum([factorials[n] / (factorials[k] * factorials[n-k])
                for k in range(m, n+1)])


with open("input.txt", 'r') as f:
    n, m = map(int, f.readline().split())

with open("output.txt", 'w') as out:
    out.write(str(count_subsets(n, m) % 1000000))