class Node:
    label = 0

    @classmethod
    def get_label(cls):
        cls.label += 1
        return cls.label


    def __init__(self, label, parent=None):
        self.label = label
        self.parent = parent
        self.children = {}


    def process_letter(self, letter):
        if letter in self.children:
            return self.children[letter], None
        new_node = Node(Node.get_label(), self)
        self.children[letter] = new_node
        edge = str(self.label) + " " + str(new_node.label) + " " + letter
        return new_node, edge


def construct_trie(strings):
    root = Node(Node.get_label())
    edges = []
    for string in strings:
        cur = root
        for c in string:
            cur, edge = cur.process_letter(c)
            if edge:
                edges.append(edge)
    return edges


with open("input.txt", 'r') as f:
    strings = []
    for line in f.readlines():
        strings.append(line.strip())

with open("output.txt", 'w') as out:
    out.write("\n".join(construct_trie(strings)))

