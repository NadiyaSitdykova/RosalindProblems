def expected_values(N, ps):
    return [N * p for p in ps]


with open("input.txt", 'r') as f:
    N = int(f.readline())
    ps = map(float, f.readline().strip().split())

with open("output.txt", 'w') as out:
    out.write(" ".join(map(str, expected_values(N, ps))))