from collections import defaultdict

def get_lines(input: str) -> list:
    with open(input) as f:
        return f.read().rstrip().split('\n')

def part1(lines: list[str]):
    graph = defaultdict(list)
    for line in lines:
        left, right = line.split(' -> ')
        graph[right].append(left)

    print(graph)

    def dfs(node: str):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)
    visited = set()
    dfs('a')

def part2(lines: list[str]):
    pass

if __name__ == '__main__':
    lines = get_lines('07.txt')
    part1(lines)
    # part2(lines)