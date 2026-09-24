from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("DFS Traversal:")
dfs(graph, "A")

print("\nBFS Traversal:")
bfs(graph, "A")

print("\n\nComplexity:")
print("DFS - Best: O(V + E), Average: O(V + E), Worst: O(V + E)")
print("BFS - Best: O(V + E), Average: O(V + E), Worst: O(V + E)")