"""Shared maze utilities for Meetings 13-15. Do not modify these during the labs.
Coordinates are (row, column); neighbor order is up, right, down, left.
"""
from pathlib import Path

DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))
MAZE_DIR = Path(__file__).resolve().parents[1] / "data" / "mazes"

def load_maze(name):
    path = MAZE_DIR / name
    rows = path.read_text(encoding="utf-8").splitlines()
    if not rows or not rows[0] or any(len(row) != len(rows[0]) for row in rows):
        raise ValueError("Maze must be nonempty and rectangular")
    if any(ch not in ".#SG" for row in rows for ch in row):
        raise ValueError("Unexpected maze symbol")
    starts = [(r,c) for r,row in enumerate(rows) for c,ch in enumerate(row) if ch == "S"]
    goals = [(r,c) for r,row in enumerate(rows) for c,ch in enumerate(row) if ch == "G"]
    if len(starts) != 1 or len(goals) != 1:
        raise ValueError("Maze must contain exactly one S and one G")
    return rows, starts[0], goals[0]

def neighbors(maze, pos):
    r,c = pos
    result = []
    for dr,dc in DIRECTIONS:
        nr,nc = r+dr,c+dc
        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] != "#":
            result.append((nr,nc))
    return result

def reconstruct_path(parents, start, goal):
    """Return path including endpoints, or None when goal is unreachable."""
    if goal not in parents:
        return None
    path=[]
    current=goal
    while current is not None:
        path.append(current)
        current=parents[current]
    path.reverse()
    if not path or path[0] != start:
        raise ValueError("Invalid parent chain")
    return path

def validate_path(maze, path, start, goal):
    if path is None: return False
    return bool(path) and path[0] == start and path[-1] == goal and all(
        maze[r][c] != "#" and (i == 0 or abs(r-path[i-1][0])+abs(c-path[i-1][1]) == 1)
        for i,(r,c) in enumerate(path))
