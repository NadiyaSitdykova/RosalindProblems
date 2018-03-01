def read_graph(graph_file):
    graph = {}
    n = int(graph_file.readline())
    for i in range(n):
        graph[i] = []
    for line in graph_file.readlines():
        u, v = map(lambda x: int(x)-1, line.split())
        graph[u].append(v)
        graph[v].append(u)
    return graph


def dfs(u, graph, visited):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v, graph, visited)


def completing_tree(g):
    visited = [False for _ in range(len(g))]
    components = 0
    while False in visited:
        u = visited.index(False)
        dfs(u, g, visited)
        components += 1
    return components - 1


with open("input.txt", 'r') as f:
    g = read_graph(f)

with open("output.txt", 'w') as out:
    out.write(str(completing_tree(g)))