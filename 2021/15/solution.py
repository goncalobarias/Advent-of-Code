from dijkstar import Graph, find_path

data = [list(map(int, list(line.strip()))) for line in open("input.txt", "r")]
start_dim = len(data)
dim = start_dim * 5
caves = [[0 for _ in range(dim)] for _ in range(dim)]
for w in range(5):
    for q in range(5):
        for i in range(start_dim):
            for j in range(start_dim):
                caves[w * start_dim + i][q * start_dim + j] = (
                    data[i][j] + w + q - 1
                ) % 9 + 1


def get_graph(g, d):
    graph = Graph()
    for i in range(d):
        for j in range(d):
            index = d * i + j
            if i - 1 >= 0:
                graph.add_edge(index, index - d, g[i - 1][j])
            if j - 1 >= 0:
                graph.add_edge(index, index - 1, g[i][j - 1])
            if i + 1 < d:
                graph.add_edge(index, index + d, g[i + 1][j])
            if j + 1 < d:
                graph.add_edge(index, index + 1, g[i][j + 1])
    return graph


# PART 1
print(
    "Answer to part 1 is",
    find_path(get_graph(data, start_dim), 0, start_dim**2 - 1).total_cost,
)

# PART 2
print(
    "Answer to part 2 is",
    find_path(get_graph(caves, dim), 0, dim**2 - 1).total_cost,
)
