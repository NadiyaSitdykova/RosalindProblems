def set_operations(a, b, n):
    full = {x for x in range(1, n+1)}
    union = a | b
    intersection = a & b
    difference1 = a - b
    difference2 = b - a
    a_complement = full - a
    b_complement = full - b
    return [union, intersection, difference1,
            difference2, a_complement, b_complement]


with open("input.txt", 'r') as f:
    n = int(f.readline())
    a, b = set(), set()
    for elem in map(int, f.readline().strip()[1:-1].split(",")):
        a.add(elem)
    for elem in map(int, f.readline().strip()[1:-1].split(",")):
        b.add(elem)

with open("output.txt", 'w') as out:
    out.write("\n".join(map(str, set_operations(a, b, n))))