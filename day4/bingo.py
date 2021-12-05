import sys
from collections import defaultdict
from dataclasses import dataclass
from typing import NewType, Dict, Tuple, List, Optional


@dataclass
class BingoSquare:
    num: int
    marked: bool


_BingoBoard = NewType('_BingoBoard', List[List[BingoSquare]])


class BingoBoard:
    def __init__(self, data: List[str]):
        self._board = self._make_board(data)

    @property
    def won(self) -> bool:
        row_complete = any([all(square.marked for square in row) for row in self._board])
        column_complete = any([all(square.marked for square in column) for column in zip(*self._board)])
        return row_complete or column_complete

    @property
    def unmarked(self) -> List[int]:
        return [
            square.num
            for row in self._board
            for square in row
            if not square.marked
        ]

    def _make_board(self, data: List[str]) -> _BingoBoard:
        board = []
        for row in data:
            parsed_row = [
                BingoSquare(num=int(n), marked=False)
                for n in row.strip().split(" ") if n
            ]
            board.append(parsed_row)
        return board

    def mark(self, n: int) -> None:
        for row in self._board:
            for square in row:
                if square.num == n:
                    square.marked = True


def play(numbers: List[int], boards: List[BingoBoard]) -> Optional[Tuple[int, BingoBoard]]:
    for n in numbers:
        for b in boards:
            b.mark(n)
            if b.won:
                return n, b
    return None


def parse_input(input_filename: str) -> Tuple[List[int], List[BingoBoard]]:
    with open(input_filename) as input_file:
        numbers = [int(ns) for ns in next(input_file).strip().split(",")]
        boards = []
        this_board_data = []
        for line in input_file:
            if line.strip():
                this_board_data.append(line)
            else:
                if this_board_data:
                    boards.append(BingoBoard(this_board_data))
                this_board_data = []
        if this_board_data:
            boards.append(BingoBoard(this_board_data))
        return numbers, boards
        

if __name__ == "__main__":
    numbers, boards = parse_input(sys.argv[1])
    result = play(numbers, boards)
    if result is None:
        print("No board won")
    else:
        last_number, winning_board = result
        print(last_number * sum(winning_board.unmarked))

