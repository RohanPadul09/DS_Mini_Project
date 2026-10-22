
import random

ROWS = 10
COLS = 10

# Wall indexes: top, right, bottom, left
TOP, RIGHT, BOTTOM, LEFT = 0, 1, 2, 3

# All walls are initially present
walls = [
    [[True, True, True, True] for _ in range(COLS)]
    for _ in range(ROWS)
]

visited = [
    [False for _ in range(COLS)]
    for _ in range(ROWS)
]


def get_neighbours(r, c):
    neighbours = []

    directions = [
        (-1, 0, TOP, BOTTOM),
        (0, 1, RIGHT, LEFT),
        (1, 0, BOTTOM, TOP),
        (0, -1, LEFT, RIGHT)
    ]

    for dr, dc, wall_here, wall_next in directions:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < ROWS and 0 <= nc < COLS:
            if not visited[nr][nc]:
                neighbours.append(
                    (nr, nc, wall_here, wall_next)
                )

    return neighbours


def generate_maze():
    stack = [(0, 0)]
    visited[0][0] = True

    while stack:
        r, c = stack[-1]
        neighbours = get_neighbours(r, c)

        if neighbours:
            nr, nc, wall_here, wall_next = random.choice(
                neighbours
            )

            # Remove the wall between adjacent cells
            walls[r][c][wall_here] = False
            walls[nr][nc][wall_next] = False

            visited[nr][nc] = True
            stack.append((nr, nc))

        else:
            # Backtrack when no neighbour is available
            stack.pop()


def display_maze():
    # Print the top border
    print("+" + "---+" * COLS)

    for r in range(ROWS):
        row = ""

        for c in range(COLS):
            if walls[r][c][LEFT]:
                row += "|"
            else:
                row += " "

            if (r, c) == (0, 0):
                row += " S "
            elif (r, c) == (ROWS - 1, COLS - 1):
                row += " E "
            else:
                row += "   "

        row += "|"
        print(row)

        bottom = ""
        for c in range(COLS):
            bottom += "+"
            bottom += "---" if walls[r][c][BOTTOM] else "   "

        bottom += "+"
        print(bottom)


if __name__ == "__main__":
    generate_maze()
    print("MAZE GENERATION USING DFS")
    print("S = Start, E = Exit")
    display_maze()
