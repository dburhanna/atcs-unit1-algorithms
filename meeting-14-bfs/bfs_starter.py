"""Meeting 14: implement BFS using collections.deque.
Run from any directory: python meeting-14-bfs/bfs_starter.py
"""
import sys
from pathlib import Path
from collections import deque
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from navigation.maze_utils import load_maze, neighbors, reconstruct_path, validate_path
from navigation.maze_visualizer import display_maze

def bfs(maze, start, goal):
    """Return (path, visited, max_frontier); path is None if unreachable.
    visited: set of expanded positions. Path includes start and goal.
    """
    frontier = deque([start])
    visited = set()
    parents = {start: None}
    max_frontier = 1
    # TODO: remove oldest position with popleft(), skip repeated expansions.
    # TODO: discover neighbors in up/right/down/left order.
    # TODO: mark nodes as discovered when enqueued to prevent duplicates.
    # TODO: reconstruct shortest path when goal is found.
    raise NotImplementedError("Implement BFS")

if __name__ == "__main__":
    maze, start, goal = load_maze("maze_01_simple.txt")
    path, visited, maximum = bfs(maze, start, goal)
    display_maze(maze, path, visited)
    print("Found:", path is not None, "Moves:", None if path is None else len(path)-1,
          "Explored:", len(visited), "Max frontier:", maximum)
    assert path is None or validate_path(maze, path, start, goal)
