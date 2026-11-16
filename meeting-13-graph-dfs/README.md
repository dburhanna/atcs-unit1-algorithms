# Meeting 13 - Graph Fundamentals and DFS
**Question:** How can a robot explore a maze without revisiting locations indefinitely?

1. Read the graph/DFS lesson in your Unit 1 workbook.
2. Review `navigation/maze_utils.py` and inspect the mazes in `data/mazes/`.
3. Create Issue: `Implement DFS maze navigation` and branch `feature/dfs-navigation`.
4. Implement `dfs()` in `dfs_starter.py`. Do not change the shared maze format.
5. Test simple, branching, dead-end, unreachable, and large mazes.
6. Record found, moves, explored nodes, and max frontier for each maze.
7. Explain how the stack, visited set, and parent dictionary have different jobs.
8. Commit code, tests, and observations; open one PR.

**Conventions:** 4-direction moves, unit cost, coordinates `(row, column)`, neighbors up/right/down/left. Since a stack is LIFO, pushing in this order explores the last pushed neighbor first.
