class Node:

    def __init__(self, parent, seq_num, start, end, set_visited=False):
        self.parent = parent
        self.kids = {}
        self.seq_info = (seq_num, start, end)
        self.visited = 0
        if set_visited:
            self.visited = set_bit(self.visited, seq_num)

    @classmethod
    def Root(cls):
        return cls(None, 0, 0, 0)

    @classmethod
    def Leaf(cls, parent, seq_num, start, end):
        return cls(parent, seq_num, start, end, set_visited=True)

def set_bit(mask, i):
    return mask | (1 << i)

def is_full_mask(mask, n):
    return mask == (1 << len (seqs)) - 1

def construct_tree(root, seqs):
    for i in range(len(seqs)):
        for start_index in range(len(seqs[i])):
            print("seq" + str(i) + " subseq" + str(start_index))
            #add suffix seq[i][j:]
            u = root
            j = start_index
            while j < len(seqs[i]) and seqs[i][j] in u.kids:
                v = u.kids[seqs[i][j]]
                k = j
                p, start, end = v.seq_info
                t = start
                #should go at least once
                while k < len(seqs[i]) and t < end and seqs[i][k] == seqs[p][t]:
                    k += 1
                    t += 1
                if t == end:
                    # no mismatch until the end of current edge
                    j = k
                    if k == len(seqs[i]):
                        # such suffix already exists, we are at leaf, so just need to update visited
                        v.visited = set_bit(v.visited, i)
                        break
                    else:
                        # current edge ended before our suffix, go to process next node
                        u = v
                else:
                    # mismatch found, need to create intermediate node
                    w = Node(u, i, j, k)
                    v.seq_info = (p, t, end)
                    v.parent = w
                    w.kids[seqs[p][t]] = v
                    u.kids[seqs[i][j]] = w
                    u = w
            if j < len(seqs[i]):
                # suffix mismatched at some point, need to create a leaf
                u.kids[seqs[i][j]] = Node.Leaf(u, i, j, len(seqs[i]))


def visit_node(u):
    for k, v in u.kids.items():
        u.visited |= visit_node(v)
    return u.visited


def find_max_subseq(u, seqs, cur_seq):
    if not is_full_mask(u.visited, len(seqs)):
        return ""
    else:
        seq_num, start, end = u.seq_info
        cur_seq += seqs[seq_num][start:end]
        cur_seq = filter(lambda c:c!='$', cur_seq)
        return max([cur_seq] + [find_max_subseq(v, seqs, cur_seq) for (_, v) in u.kids.items()], key=len)


def find_shared_motif(seqs):
    suffix_tree = Node.Root()
    construct_tree(suffix_tree, seqs)
    visit_node(suffix_tree)
    return find_max_subseq(suffix_tree, seqs, "")


with open("input.txt", 'r') as file:
    seqs = []
    s = ""
    for line in file.readlines():
        if line[0] == ">":
            if len(s) > 0:
                seqs.append(s + "$")
                s = ""
        else:
            s += line.strip()
    seqs.append(s + "$")
    print(seqs)

with open("output.txt", 'w') as out:
    out.write(find_shared_motif(seqs))

