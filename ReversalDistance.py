def reversal(p, l, r):
    return p[:l] + p[l:r+1][::-1] + p[r+1:]


def compute_distance(p1, p2):
    if p1 == p2:
        return 0
    l, r = 0, len(p1)-1
    while p1[l] == p2[l]:
        l += 1
    while p1[r] == p2[r]:
        r -= 1
    p1 = p1[l:r+1]
    p2 = p2[l:r+1]
    l = p2.index(p1[-1])
    r = p2.index(p1[0])
    return 1 + min(compute_distance(p1, reversal(p2, 0, r)),
                   compute_distance(p1, reversal(p2, l, len(p2)-1)))


def reversal_distances(ps):
    ds = []
    for i in range(0, len(ps), 2):
        ds.append(compute_distance(ps[i], ps[i + 1]))
    return ds


with open("input.txt", 'r') as f:
    ps = []
    for line in f.readlines():
        ps.append(map(int, line.strip().split()))

with open("output.txt", 'w') as out:
    out.write(" ".join(map(str, reversal_distances(ps))))