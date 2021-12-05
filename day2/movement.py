import sys


_depth_map = {
    "forward": lambda n, x, y: (x+n, y),
    "up": lambda n, x, y: (x, y-n),
    "down": lambda n, x, y: (x, y+n),
}


def process(input_file: str):
    pos = (0, 0)
    with open(input_file) as input_file:
        for line in input_file:
            elems = line.strip().split(" ")
            direction, value = elems[0], int(elems[1])
            pos = _depth_map[direction](value, pos[0], pos[1])
    return pos


if __name__ == "__main__":
    pos = process(sys.argv[1])
    print(pos[0] * pos[1])

