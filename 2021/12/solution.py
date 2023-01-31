from collections import deque

data = [line.strip().split("-") for line in open("input.txt", "r")]
graph = {}
for [u, v] in data:
    if u not in graph.keys():
        graph[u] = []
    if v not in graph.keys():
        graph[v] = []
    graph[u] += [v]
    graph[v] += [u]


def caves_path_calculator(caves_queue, part, visited=False):
    paths = 0
    if caves_queue[-1] == "end":
        return 1

    for v in graph[caves_queue[-1]]:
        if v == "start":
            continue
        if (part == 1 or visited) and "a" <= v[0] <= "z" and v in caves_queue:
            continue
        if "a" <= v[0] <= "z" and v in caves_queue:
            visited = True

        caves_queue.append(v)
        paths += caves_path_calculator(caves_queue, part, visited)
        v = caves_queue.pop()
        if "a" <= v[0] <= "z" and v in caves_queue:
            visited = False

    return paths


# PART 1
print("Answer to part 1 is", caves_path_calculator(deque(["start"]), 1))

# PART 2
print("Answer to part 2 is", caves_path_calculator(deque(["start"]), 2))
