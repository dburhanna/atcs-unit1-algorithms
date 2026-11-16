"""ASCII visualization: '*' path, '+' visited, # wall, S/G endpoints."""
def display_maze(maze, path=None, visited=None):
    path_set=set(path or [])
    visited_set=set(visited or [])
    for r,row in enumerate(maze):
        output=[]
        for c,ch in enumerate(row):
            pos=(r,c)
            if ch in "SG#": output.append(ch)
            elif pos in path_set: output.append("*")
            elif pos in visited_set: output.append("+")
            else: output.append(ch)
        print("".join(output))
