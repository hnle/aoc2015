"""
https://adventofcode.com/2015/day/10

"""
def day10(s: str, times: int) -> int:
    for _ in range(times):
        # print(f'{k+1=}, {s}')
        i = 0
        n = len(s)
        buf = []
        while i < n:
            j = i+1
            count = 1
            while j < n and s[j] == s[i]:
                j += 1
                count += 1
            buf.append(str(count))
            buf.append(s[i])
            i = j
        if i < j:
            buf.append(str(count))
            buf.append(s[i])
        s = ''.join(buf)

    return len(s)

def test_part1():
    data = [
        ('1', 2),
        ('11', 2),
        ('21', 4),
        ('1211', 6),
        ('111221', 6),
        ('1113222113', 10)  # 3113322113
    ]
    for s, expected in data:
        actual = day10(s)
        try:
            assert actual == expected
        except AssertionError:
            print(f'{s=}, {actual=}, {expected=}')

if __name__ == '__main__':
    print(day10('1113222113', 50))

