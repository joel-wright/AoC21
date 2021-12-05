import sys
from collections import deque


class Window:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def push(self, elem):
        bigger = elem > self._a
        self._a = self._b
        self._b = self._c
        self._c = elem
        return int(bigger)


def process(filename: str) -> int:
    deeper_count = 0
    with open(filename) as input:
        window = Window(int(next(input)), int(next(input)), int(next(input)))
        for line in input:
            new_depth = int(line.strip())
            deeper_count += window.push(new_depth)
    return deeper_count


if __name__ == "__main__":
    c = process(sys.argv[1])
    print(c)

