def get_lines(input: str) -> list:
    with open(input) as f:
        return f.read().rstrip().split('\n')

def part1(lines: list[str]):
    def num_chars_for_values(s: str) -> int:
        count = 0
        escaping = False
        i = 0
        while i < len(s):
            c = s[i]
            if c == '\\':
                escaping = True
            else:
                if escaping:
                    # print(f'{s=}, {i=}, {s[i]=}')
                    if s[i] == '\\' or s[i] == '"':  #
                        i += 1
                    elif s[i] == 'x':
                        i += 2
                    escaping = False
                count += 1
            i += 1
        return count

    # def test():
    #     assert num_chars_for_values('') == 0
    #     assert num_chars_for_values('abc') == 3
    #     assert num_chars_for_values('aaa\"aaa') == 7
    #     assert num_chars_for_values('\x27') == 1
    #     assert num_chars_for_values('\\xa8br\\x8bjr\\"') == 7
    # test()

    sum_diffs = 0
    for line in lines:
        num_chars_of_code = len(line)
        sum_diffs += num_chars_of_code - num_chars_for_values(line[1:-1])

    return sum_diffs


def part2(lines: list[str]):
    pass

if __name__ == '__main__':
    lines = get_lines('08.txt')
    print(part1(lines))
    # part2(lines)
