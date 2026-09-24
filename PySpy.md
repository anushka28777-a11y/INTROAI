# Py-Spy Profiling

Install py-spy:

    pip install py-spy

Run the program with py-spy:

    py-spy top -- python dfs_bfs.py

Record a profile:

    py-spy record -o dfs_bfs.svg -- python dfs_bfs.py

The generated SVG can be opened in a browser to inspect function activity and execution time.

## Complexity

| Algorithm | Best Case | Average Case | Worst Case |
|---|---|---|---|
| DFS | O(V + E) | O(V + E) | O(V + E) |
| BFS | O(V + E) | O(V + E) | O(V + E) |