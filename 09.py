from collections import defaultdict
from itertools import permutations

def get_lines(input: str) -> list:
    with open(input) as f:
        return f.read().rstrip().split('\n')

def part1(lines: list[str]):
    graph = defaultdict(list)
    distances = {}
    for line in lines:
        parts = line.split(' = ')
        c1, c2 = parts[0].split(' to ')
        graph[c1].append(c2)
        graph[c2].append(c1)
        distances[(c1, c2)] = int(parts[1])
        distances[(c2, c1)] = int(parts[1])
    # print(graph)
    # print(len(graph))
    # print(distances)
    paths = []
    for i, path in enumerate(permutations(graph)):
        distance = 0
        for loc1, loc2 in zip(path[:-1], path[1:]):
            distance += distances[(loc1, loc2)]

        paths.append((distance, path))
        # print distance, path

    paths.sort()
    print("Shortest path:")
    print(paths[0])
    print(paths[2])
    print(paths[4])
    print()

    print("Longest path:")
    print(paths[-1])
    print(paths[-3])
    print(paths[-5])

def part2(lines: list[str]):
    pass

if __name__ == '__main__':
    lines = get_lines('09.txt')
    part1(lines)
    # part2(lines)
