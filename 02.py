"""
https://adventofcode.com/2015/day/2
Run as: python3 02.py < 02.txt
"""
if __name__ == '__main__':
    with open(0) as f:
        lines = f.read().split('\n')
    part1 = 0
    part2 = 0
    for dims in lines:
        l, w, h = sorted(list(map(int, dims.split('x'))))
        # print(l, w, h)
        a1, a2, a3 = l*w, w*h, h*l
        part1 += 2*(a1 + a2 + a3) + a1
        part2 += 2*(l + w) + l*w*h
    print(part1)
    print(part2)