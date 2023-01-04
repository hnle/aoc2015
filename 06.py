"""
Part 1:

"""
import re
OFF = 0
ON = 1

def turn(grid, r1: int, c1: int, r2: int, c2: int, to_state: int, part) -> None:
    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            if part == 1:
                if grid[r][c] != to_state:
                    grid[r][c] = to_state
            else:
                if to_state == 1:
                    grid[r][c] += 1
                else:
                    if grid[r][c] > 0:
                        grid[r][c] -= 1

def toggle(grid, r1: int, c1: int, r2: int, c2: int, part) -> None:
    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            if part == 1:
                grid[r][c] = 1 - grid[r][c]
            else:
                grid[r][c] += 2

def count(grid):
    return sum(grid[r][c] for r in range(1000) for c in range(1000))

if __name__ == '__main__':
    with open('06.txt') as f:
        lines = f.read().rstrip().split('\n')
    pattern = r'(\d+),(\d+) through (\d+),(\d+)'

    for part in [1, 2]:
        grid = [[0] * 1000 for _ in range(1000)]
        for line in lines:
            m = re.search(pattern, line)
            r1, c1, r2, c2 = list(map(int, [m.group(1), m.group(2), m.group(3), m.group(4)]))
            if line.startswith('turn on'):
                turn(grid, r1, c1, r2, c2, to_state=1, part=part)
            elif line.startswith('turn off'):
                turn(grid, r1, c1, r2, c2, to_state=0, part=part)
            else:
                toggle(grid, r1, c1, r2, c2, part)
        print(count(grid))
