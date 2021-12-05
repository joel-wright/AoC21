import sys


class Sub:
    def __init__(self, position: int, depth: int, aim: int) -> None:
        self._position = position
        self._depth = depth
        self._aim = aim

    @property
    def pos_depth(self) -> int:
        return self._position * self._depth

    def move(self, motion: str, value: int) -> None:
        match motion:
            case "forward":
                self._position += value
                self._depth += self._aim * value
            case "up":
                self._aim -= value
            case "down":
                self._aim += value
            case _:
                raise RuntimeError(f"No idea what motion '{motion}' means")


def process(input_file: str) -> Sub:
    s = Sub(0, 0, 0)
    with open(input_file) as input_file:
        for line in input_file:
            elems = line.strip().split(" ")
            direction, value = elems[0], int(elems[1])
            s.move(direction, value)
    return s


if __name__ == "__main__":
    s = process(sys.argv[1])
    print(s.pos_depth)

