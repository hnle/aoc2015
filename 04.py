import hashlib

def solve(key, zeroes):
    n = 1
    prefix = zeroes * '0'
    while True:
        s = key + str(n)
        h = hashlib.md5(s.encode()).hexdigest()[:zeroes]
        if h == prefix:
            return n
        n += 1

if __name__ == '__main__':
    print(solve('iwrupvqb', 5))
    print(solve('iwrupvqb', 6))
