import sys


def process(filename: str) -> int:
    deeper_count = 0
    with open(filename) as input:
        depth = None
        for line in input:
            new_depth = int(line.strip())
            if depth is not None and new_depth > depth:
                deeper_count += 1
            depth = new_depth
    return deeper_count


if __name__ == "__main__":
    c = process(sys.argv[1])
    print(c)

