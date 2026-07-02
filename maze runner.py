import heapq

maze = [
    ['S', '.', '.', '.', '#'],
    ['#', '#', '.', '#', '.'],
    ['.', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.'],
    ['.', '#', '#', '#', '.'],
    ['.', '.', '.', 'G', '.']
]

ROWS = len(maze)
COLS = len(maze[0])

# Find Start and Goal
start = None
goal = None

for r in range(ROWS):
    for c in range(COLS):
        if maze[r][c] == 'S':
            start = (r, c)
        elif maze[r][c] == 'G':
            goal = (r, c)

# Manhattan Distance Heuristic
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Algorithm
def astar(start, goal):

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}

    g_score = {start: 0}

    while open_set:

        current = heapq.heappop(open_set)[1]

        if current == goal:

            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            return path

        row, col = current

        directions = [
            (-1, 0),   # Up
            (1, 0),    # Down
            (0, -1),   # Left
            (0, 1)     # Right
        ]

        for dr, dc in directions:

            nr = row + dr
            nc = col + dc

            if (
                0 <= nr < ROWS and
                0 <= nc < COLS and
                maze[nr][nc] != '#'
            ):

                neighbor = (nr, nc)

                tentative_g = g_score[current] + 1

                if (
                    neighbor not in g_score or
                    tentative_g < g_score[neighbor]
                ):

                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g

                    f_score = (
                        tentative_g +
                        heuristic(neighbor, goal)
                    )

                    heapq.heappush(
                        open_set,
                        (f_score, neighbor)
                    )

    return None

# Run A*
path = astar(start, goal)

print("\n" + "=" * 50)
print("MAZE SOLVER USING A* SEARCH")
print("=" * 50)

if path:

    print("\nShortest Path Found!\n")

    print("Path Coordinates:")

    for step in path:
        print(step)

    print("\nPath Length =", len(path) - 1)

    # Visualize Path
    for r, c in path:
        if maze[r][c] not in ['S', 'G']:
            maze[r][c] = '*'

    print("\nMaze Visualization:\n")

    for row in maze:
        print(" ".join(row))

else:

    print("\nGoal is Unreachable!")