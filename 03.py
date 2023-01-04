"""
https://adventofcode.com/2015/day/3
Run as: python3 03.py < 03.txt
"""

def _new_pos(d, x, y):
    if d == '>':
        x += 1
    elif d == '<':
        x -= 1
    elif d == '^':
        y += 1
    else:
        y -= 1
    return x, y

def part1(line):
    visited = set([(0, 0)])
    x, y = 0, 0
    for d in line:
        x, y = _new_pos(d, x, y)
        visited.add((x, y))
    return len(visited)

def part2(line):
    visited = set([(0, 0)])
    x1, y1, x2, y2 = 0, 0, 0, 0
    for i in range(0, len(line)-1, 2):
        d = line[i]
        x1, y1 = _new_pos(d, x1, y1)
        visited.add((x1, y1))
        d = line[i+1]
        x2, y2 = _new_pos(d, x2, y2)
        visited.add((x2, y2))

    return len(visited)
if __name__ == '__main__':
    with open(0) as f:
        line = f.read().rstrip()

    print(part1(line))
    print(part2(line))
