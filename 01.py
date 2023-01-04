if __name__ == '__main__':
    with open('01.txt') as f:
        line = f.readline().rstrip()
    floor = 0
    for i, c in enumerate(line):
        if c == '(':
            floor += 1
        else:
            floor -= 1
            if floor == -1:
                print(i+1)
    print(floor)
