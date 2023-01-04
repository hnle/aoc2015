"""
https://adventofcode.com/2015/day/5
Part 1:
A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of
the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules
overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?

--- Part Two ---
Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping,
  like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them,
  like xyx, abcdefeghi (efe), or even aaa.

For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats
  with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between,
  even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?
"""
from collections import Counter
VOWELS = set('aeiou')
DISALLOWED = set(['ab', 'cd', 'pq', 'xy'])

def num_nice_strings1(lines: list[str]) -> int:
    def count_vowels(s: str) -> int:
        return sum(c in VOWELS for c in s)

    def has_double_letters(s: str) -> bool:
        return any(s[i] == s[i+1] for i in range(len(s) - 1))

    def has_disallowed_substring(s: str) -> bool:
        return any(s[i:i+2] for i in range(len(s)-1) if s[i:i+2] in DISALLOWED)

    return sum(count_vowels(s) >= 3 and has_double_letters(s) and not has_disallowed_substring(s) for s in lines)

def has_pair_appear_at_least_twice(s: str) -> bool:
    pairs = Counter()
    # pairs starting from index 0
    for i in range(0, len(s)-1, 2):
        for j in range(i+2, len(s)):
            if s[i:i+2] == s[j:j+2]:
                return True

    for i in range(1, len(s)-1, 2):
        for j in range(i+2, len(s)):
            if s[i:i+2] == s[j:j+2]:
                return True
    return False

def has_sandwich_with_one_letter(s: str) -> bool:
    return any(s[i] == s[i+2] for i in range(len(s)-2))

def num_nice_strings2(lines: list[str]) -> int:
    return sum(has_pair_appear_at_least_twice(s) and has_sandwich_with_one_letter(s) for s in lines)

# if __name__ == '__main__':
#     print(count_vowels('ugknbfddgicrmopn'))
#     print(has_double_letters('jchzalrnumimnmhp'))
#     print(has_disallowed_substring('haegwjzuvuyypxyu'))

if __name__ == '__main__':
    with open('./05.txt') as f:
        lines = f.read().rstrip().split('\n')
    # print(num_nice_strings1(lines))
    print(num_nice_strings2(lines))
    # assert has_pair_appear_at_least_twice('qjhvhtzxzqqjkmpb')
    # assert has_pair_appear_at_least_twice('xxyxx')
    # assert has_pair_appear_at_least_twice('uurcxstgmygtbstg')
    # assert not has_pair_appear_at_least_twice('ieodomkazucvgmuy')
    # assert has_sandwich_with_one_letter('xyx')
    # assert has_sandwich_with_one_letter('abcdefeghi')