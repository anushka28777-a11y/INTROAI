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

print("\n\nBFS Traversal:")
bfs(graph, "A")

print("\n\nTime Complexity:")
print("----------------")
print("DFS:")
print("  Best Case    : O(V + E)")
print("  Average Case : O(V + E)")
print("  Worst Case   : O(V + E)")

print("\nBFS:")
print("  Best Case    : O(V + E)")
print("  Average Case : O(V + E)")
print("  Worst Case   : O(V + E)")
