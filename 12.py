def get_lines(input: str) -> list:
    with open(input) as f:
        return f.read().rstrip().split('\n')

def part1(s: str):
    sign = 1
    curr = 0
    total = 0
    for c in s:
        if c == '-':
            sign = -1
        elif c in '0123456789':
            curr = 10*curr + int(c)
        else:
            total += sign * curr
            curr = 0
            sign = 1
    if curr > 0:
        total += sign * curr
    return total


def test_part1():
    data = [
        ('[]', 0),
        ('{}', 0),
        ('[1,2,3]', 6),
        ('{"a":2,"b":4}', 6),
        ('[[[3]]]', 3),
        ('{"a":{"b":4},"c":-1}', 3),
        ('{"a":[-1,1]}', 0),
        ('[-1,{"a":1}]', 0)

    ]
    for s, expected in data:
        actual = part1(s)
        try:
            assert actual == expected
        except AssertionError:
            print(f'{s=}, {expected=}, {actual=}')

def part2(s: str) -> int:
    sign = 1
    curr = 0
    total = 0
    n = len(s)
    print(n)
    i = 0
    while i < n:
        c = s[i]
        level = 0
        if c == '{':  # start of an object
            stack = [c]
            level += 1
            j = i + 1
            while level > 0:
                while j < n and s[j] != '}':
                    stack.append(s[j])
                    if s[j] == '{':
                        level += 1
                    j += 1
                # Now pop everything until seeing '{'
                buf = []
                while stack[-1] != '{':
                    buf.append(stack.pop())
                stack.pop()  # pop the '{'
                level -= 1
                t = ''.join(reversed(buf))
                print(t)
                if ':"red"' not in t:
                    total += part1(t)

            i = j + 1
            continue
        elif c == '-':
            sign = -1
        elif c in '0123456789':
            curr = 10*curr + int(c)
        else:
            total += sign * curr
            curr = 0
            sign = 1
        i += 1
    if curr > 0:
        total += sign * curr
    return total

def test_part2():
    data = [
        ('[1,{"c":"red","b":2},3]', 4),
        ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
        ('[1,"red",5]', 6)
    ]
    for s, expected in data:
        actual = part2(s)
        try:
            assert actual == expected
        except AssertionError:
            print(f'{s=}, {expected=}, {actual=}')

def simplify(line: str) -> str:
    import re
    pattern_template = r',*"[a-z]":"{}",*'
    colors = ['blue', 'green', 'orange', 'yellow', 'violet']
    for c in colors + ['red']:
        line = line.replace(f',"{c}"', '').replace(f'"{c}",', '')
    for c in colors:
        line = re.sub(pattern_template.format(c), '', line)
    print(line.count('red'))
    return line

if __name__ == '__main__':
    # test_part2()
    lines = get_lines('12.txt')
    line = lines[0]
    # print(part1(line))
    # print(part2(line))
    print(simplify(line))
    print(part2(simplify((line))))
