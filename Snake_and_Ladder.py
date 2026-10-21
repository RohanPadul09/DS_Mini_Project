from collections import deque

SIZE = 30

snakes = {
    17: 4,
    19: 7,
    27: 1
}

ladders = {
    3: 22,
    5: 8,
    11: 26,
    20: 29
}

def get_position(pos):
    if pos in snakes:
        print("Snake! Go down from", pos, "to", snakes[pos])
        return snakes[pos]

    if pos in ladders:
        print("Ladder! Climb from", pos, "to", ladders[pos])
        return ladders[pos]

    return pos


def snake_ladder_bfs():
    queue = deque()
    queue.append((1, 0, [1]))

    visited = set()
    visited.add(1)

    while queue:
        pos, moves, path = queue.popleft()

        if pos == SIZE:
            print("\nGame completed!")
            print("Path:", path)
            print("Minimum dice throws:", moves)
            return

        for dice in range(1, 7):
            next_pos = pos + dice

            if next_pos <= SIZE:
                next_pos = get_position(next_pos)

                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append(
                        (next_pos, moves + 1, path + [next_pos])
                    )

    print("Destination cannot be reached.")


print("===== SNAKE AND LADDER GAME =====")
print("Starting position: 1")
print("Destination:", SIZE)

snake_ladder_bfs()
