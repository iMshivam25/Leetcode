class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set(map(tuple, obstacles))
        x, y = 0, 0
        direction = 0
        # Directions: north, east, south, west
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_distance = 0

        for command in commands:
            if command == -1:  # turn right
                direction = (direction + 1) % 4
            elif command == -2:  # turn left
                direction = (direction + 3) % 4
            else:
                dx, dy = directions[direction]
                for _ in range(command):
                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy
                        max_distance = max(max_distance, x * x + y * y)
                    else:
                        break

        return max_distance
