# Meeting 14 - BFS Shortest Paths
**Question:** How does a queue change exploration order and path length?

1. Review the Meeting 13 maze and DFS implementation.
2. Create Issue: `Implement BFS shortest-path navigation`; branch `feature/bfs-navigation`.
3. Implement `bfs()` using `collections.deque` and `popleft()`.
4. Use the same maze utility functions, movement rules, and neighbor order as DFS.
5. Record the same metrics and compare both algorithms on each maze.
6. Demonstrate BFS shortest-path behavior on these unweighted grids.
7. Document evidence, tests, and tradeoffs; open one PR.

**Fair comparison:** count a node as explored when removed from the frontier and processed. Record max frontier size as the maximum number of waiting positions. Compare path length in moves, not nodes.
