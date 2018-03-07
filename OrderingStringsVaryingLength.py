def string_varying_length(alphabet, n):
    if n == 1:
        return alphabet
    res = []
    for s in string_varying_length(alphabet, n-1):
        res.append(s)
        if len(s) == n-1:
            for symbol in alphabet:
                res.append(s + symbol)
    return res


with open("input.txt", 'r') as f:
    alphabet = f.readline().strip().split()
    n = int(f.readline())

with open("output.txt", 'w') as out:
    out.write("\n".join(string_varying_length(alphabet, n)))