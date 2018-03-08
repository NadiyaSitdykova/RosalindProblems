def is_pair(bp1, bp2):
    return (bp1 == "A" and bp2 == "U") \
           or (bp1 == "U" and bp2 == "A") \
           or (bp1 == "C" and bp2 == "G") \
           or (bp1 == "G" and bp2 == "C") \
           or (bp1 == "G" and bp2 == "U") \
           or (bp1 == "U" and bp2 == "G")


def non_crossing_matchings(s, d):
    if len(s) == 0:
        return 1
    if s not in d:
        d[s] = sum([int(is_pair(s[0], s[k]))
                    * non_crossing_matchings(s[1:k], d)
                    * non_crossing_matchings(s[k + 1:], d)
                    for k in range(4, len(s))]) \
               + non_crossing_matchings(s[1:], d)
    return d[s]


with open("input.txt", 'r') as f:
    s = f.readline().strip()

with open("output.txt", 'w') as out:
    out.write(str(non_crossing_matchings(s, {})))