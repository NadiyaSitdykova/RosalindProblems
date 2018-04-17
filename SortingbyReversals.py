def reversal(p, l, r):
    return p[:l] + p[l:r+1][::-1] + p[r+1:]


def sorting_by_reversals(p1, p2, revs):
    if p1 == p2:
        return 0, revs
    l1, r1 = 0, len(p1)-1
    while p1[l1] == p2[l1]:
        l1 += 1
    while p1[r1] == p2[r1]:
        r1 -= 1
    l2 = p1.index(p2[r1])
    r2 = p1.index(p2[l1])

    d1, revs1 = sorting_by_reversals(reversal(p1, l1, r2), p2, revs + [(l1, r2)])
    d2, revs2 = sorting_by_reversals(reversal(p1, l2, r1), p2, revs + [(l2, r1)])
    if d1 < d2:
        return d1 + 1, revs1
    return d2 + 1, revs2


with open("input.txt", 'r') as f:
    p1 = map(int, f.readline().strip().split())
    p2 = map(int, f.readline().strip().split())

d, revs = sorting_by_reversals(p1, p2, [])

with open("output.txt", 'w') as out:
    out.write(str(d) + "\n")
    out.write("\n".join(map(lambda (l, r): str(l+1) + " " + str(r+1), revs)))