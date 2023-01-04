#!/usr/bin/env python

import sys
import re
import json

infile = "day12-input"

number_re = re.compile(r"(?<![\"\d-])-?\d+(?![\"\d])")

def extract_numbers(text):
    return [int(x) for x in number_re.findall(text)]

def remove_red_objects(input_obj):
    if isinstance(input_obj, dict):
        return remove_red_objects_from_dict(input_obj)
    elif isinstance(input_obj, list):
        return remove_red_objects_from_list(input_obj)
    else:
        return input_obj

def remove_red_objects_from_dict(input_dict):
    assert isinstance(input_dict, dict)
    output_dict = {}
    if "red" not in input_dict.values():
        for k, v in input_dict.items():
            output_dict[k] = remove_red_objects(v)
    return output_dict

def remove_red_objects_from_list(input_list):
    assert isinstance(input_list, list)
    output_list = []
    for v in input_list:
        output_list.append(remove_red_objects(v))
    return output_list

def get_lines(input: str) -> list:
    with open(input) as f:
        return f.read().rstrip().split('\n')

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


def part2(input: str):
    print('Part 2')
    input_obj = json.loads(input)
    stripped_obj = remove_red_objects(input_obj)
    stripped_text = json.dumps(stripped_obj)
    numbers = extract_numbers(stripped_text)
    total = sum(numbers)
    print(f'Found {len(numbers)} numbers in the stripped input')
    print(f'Sum is {total}')


def part1(input: str):
    numbers = extract_numbers(input)
    total = sum(numbers)
    print(f'Found {len(numbers)} numbers in the input')
    print(f'Sum is {total}')


if __name__ == '__main__':
    # test_part2()
    lines = get_lines('12.txt')
    input = lines[0]
    part1(input)

    part2(input)
