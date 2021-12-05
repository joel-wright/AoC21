import sys


def process(filename: str) -> int:
    with open(filename) as input:
        lines = input.readlines()
        return sum([
            int(b > a) for (a, b) in zip(lines, lines[2:])
        ])


if __name__ == "__main__":
    c = process(sys.argv[1])
    print(c)

