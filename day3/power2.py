import sys
from collections import defaultdict
from typing import Tuple, List, Optional



_MOST_COMMON_LOOKUP = {
    "o2": True,
    "co2": False,
}
_BIT_CHOICE = {
    True: '1',
    False: '0',
}


def process(input_file: str) -> Tuple[int, int]:
    with open(input_file) as input_file:
        lines = input_file.readlines()
    
    co2_lines = [l.strip() for l in lines]
    o2_gen_lines = [l.strip() for l in lines]

    index = 0
    while len(co2_lines) > 1:
        print(co2_lines)
        co2_lines = _filter_lines(co2_lines, index, "co2")
        index += 1
    co2_num_str = co2_lines[0]
    print(f"CO2: {co2_num_str}")

    index = 0
    while len(o2_gen_lines) > 1:
        print(o2_gen_lines)
        o2_gen_lines = _filter_lines(o2_gen_lines, index, "o2")
        index += 1
    o2_gen_num_str = o2_gen_lines[0]
    print(f"O2: {o2_gen_num_str}")
    
    return int(co2_num_str, 2), int(o2_gen_num_str, 2)


def _filter_lines(lines: List[str], index: int, reading: str):
    details = defaultdict(int)
    for line in lines:
        details[line[index]] += 1
    _mlc = _common([(bit, frequency) for bit, frequency in details.items()], _MOST_COMMON_LOOKUP[reading])
    filtered = [l for l in lines if l[index] == _mlc]
    return filtered


def _common(bit_freqs: List[Tuple[str, int]], most_common: bool) -> Optional[str]:
    sorted_bit_freqs = sorted(bit_freqs, key=lambda t: t[1], reverse=most_common)
    print(sorted_bit_freqs)
    if sorted_bit_freqs[1:]:
        if sorted_bit_freqs[0][1] == sorted_bit_freqs[1][1]:
            return _BIT_CHOICE[most_common]
        else:
            return sorted_bit_freqs[0][0]
    if sorted_bit_freqs:
        return sorted_bit_freqs[0][0]
    return _BIT_CHOICE[most_common]


if __name__ == "__main__":
    co2, o2 = process(sys.argv[1])
    print(co2 * o2)

