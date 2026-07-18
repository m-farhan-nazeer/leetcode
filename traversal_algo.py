def dfs(graph, root):
    stack = []
    stack.append(root)

    visited = set()

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            print(node)

            for val in graph[node]:
                if val not in visited:
                    stack.append(val)
def bfs(graph, root):
    q = []
    q.append(root)
    visited = set()

    while q :
        node = q.pop(0)
        if node not in visited:
            visited.add(node)
            print(node)
            for val in graph[node]:
                if val not in visited:
                    q.append(val)

graph = {
    0: [1, 2],
    1: [3],
    2: [],
    3: []
}

bfs(graph, 0)