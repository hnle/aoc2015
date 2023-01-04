def get_lines(input: str) -> list:
    with open(input) as f:
        return f.read().rstrip().split('\n')

def part1(lines: list[str]):
    pass

def part2(lines: list[str]):
    pass

if __name__ == '__main__':
    lines = get_lines('0x.txt')
    part1(lines)
    part2(lines)
