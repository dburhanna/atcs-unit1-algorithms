"""Meeting 13: implement iterative DFS with a list used as a stack.
Run from any directory: python meeting-13-graph-dfs/dfs_starter.py
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from navigation.maze_utils import load_maze, neighbors, reconstruct_path, validate_path
from navigation.maze_visualizer import display_maze

def dfs(maze, start, goal):
    """Return (path, visited, max_frontier); path is None if unreachable.
    visited: set of expanded positions. Path includes start and goal.
    """
    frontier = [start]
    visited = set()
    parents = {start: None}
    max_frontier = 1
    # TODO: pop from the stack, skip already visited nodes, expand neighbors.
    # TODO: store parents when a node is FIRST discovered; avoid duplicates.
    # TODO: when goal is reached, use reconstruct_path(...).
    # TODO: return (None, visited, max_frontier) if exhausted.
    raise NotImplementedError("Implement DFS")

if __name__ == "__main__":
    maze, start, goal = load_maze("maze_01_simple.txt")
    path, visited, maximum = dfs(maze, start, goal)
    display_maze(maze, path, visited)
    print("Found:", path is not None, "Moves:", None if path is None else len(path)-1,
          "Explored:", len(visited), "Max frontier:", maximum)
    assert path is None or validate_path(maze, path, start, goal)
