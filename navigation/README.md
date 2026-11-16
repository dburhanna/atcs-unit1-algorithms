# Shared navigation utilities
`maze_utils.py` is provided infrastructure, not a student algorithm solution.

`load_maze(filename)` returns `(maze, start, goal)`.
`neighbors(maze, position)` returns traversable neighbors in **up, right, down, left** order.
`reconstruct_path(parents, start, goal)` returns a list of positions or `None`.
`validate_path(maze, path, start, goal)` checks a route.
`display_maze(maze, path, visited)` prints a text map.

Import these utilities from Meeting 13/14 starter scripts. Do not rewrite them for each algorithm.
