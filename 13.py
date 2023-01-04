"""
https://adventofcode.com/2015/day/13
--- Day 13: Knights of the Dinner Table ---
In years past, the holiday feast with your family hasn't gone so well. Not everyone gets along! This year, you resolve,
will be different. You're going to find the optimal seating arrangement and avoid all those awkward conversations.

You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they
were to find themselves sitting next to each other person. You have a circular table that will be just big enough to
fit everyone comfortably, and so each person will have exactly two neighbors.

For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows:

Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.

Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much),
but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44.

If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54).
Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41).
The arrangement looks like this:

     +41 +46
+55   David    -2
Carol       Alice
+60    Bob    +54
     -7  +83
After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal,
with a total change in happiness of 330.

What is the total change in happiness for the optimal seating arrangement of the actual guest list?
"""
from collections import defaultdict
from heapq import heappush, heapreplace
from itertools import permutations
from pprint import pp
import re
PATTERN = re.compile(r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)')

def get_lines(input: str) -> list:
    with open(input) as f:
        return f.read().rstrip().split('\n')

def part1(lines: list[str]):
    graph, happiness = make_ds(lines)
    # print(graph)
    # pp(happiness)
    paths = []
    for path in permutations(graph):
        total = 0
        path = list(path) + [path[0]]
        for p1, p2 in zip(path[:-1], path[1:]):
            total += happiness[(p1, p2)] + happiness[(p2, p1)]

        paths.append((total, path))
        # print total, path

    paths.sort()
    pp(paths)
    return paths[-1][0]

def part2(lines: list[str]):
    graph, happiness = make_ds(lines)
    # print(graph)
    # pp(happiness)
    paths = []
    n = len(graph)
    for path in permutations(graph):
        path = list(path)
        for i in range(n-1):
            total = 0
            new_path = path[:i] + ['ME'] + path[i:]
            for p1, p2 in zip(new_path[:-1], new_path[1:]):
                if p1 == 'ME' or p2 == 'ME':
                    continue
                total += happiness[(p1, p2)] + happiness[(p2, p1)]

                paths.append((total, new_path))
        # print total, path

    paths.sort()
    # pp(paths)
    return paths[-1][0]

def part1_heap(lines: list[str]) -> int:
    graph, happiness = make_ds(lines)
    max_heap = []
    for path in permutations(graph):
        total = 0
        path = list(path) + [path[0]]
        for p1, p2 in zip(path[:-1], path[1:]):
            total += happiness[(p1, p2)] + happiness[(p2, p1)]

        if not max_heap:
            heappush(max_heap, -total)
        else:
            if -total < max_heap[0]:
                heapreplace(max_heap, -total)
    return -max_heap[0]

def part2_heap(lines: list[str]):
    graph, happiness = make_ds(lines)
    max_heap = []
    n = len(graph)
    for path in permutations(graph):
        path = list(path)
        for i in range(n-1):
            total = 0
            new_path = path[:i] + ['ME'] + path[i:]
            for p1, p2 in zip(new_path[:-1], new_path[1:]):
                if p1 == 'ME' or p2 == 'ME':
                    continue
                total += happiness[(p1, p2)] + happiness[(p2, p1)]

                if not max_heap:
                    heappush(max_heap, -total)
                else:
                    if -total < max_heap[0]:
                        heapreplace(max_heap, -total)
    return -max_heap[0]

def make_ds(lines):
    graph = defaultdict(list)
    happiness = {}
    for line in lines:
        # print(line)
        m = re.match(PATTERN, line)
        if m.group(2) == 'gain':
            val = int(m.group(3))
        else:
            val = -int(m.group(3))
        graph[m.group(1)].append(m.group(4))
        happiness[(m.group(1), m.group(4))] = val
    return graph, happiness


if __name__ == '__main__':
    lines = get_lines('13.txt')
    # assert part1(lines) == 709
    # assert part1_heap(lines) == 709
    # assert part2(lines) == 668
    assert part2_heap(lines) == 668
