import sys
from collections import defaultdict
from typing import Tuple


def process(input_file: str) -> Tuple[int, int]:
    details = defaultdict(lambda: defaultdict(int))
    with open(input_file) as input_file:
        for line in input_file:
            for j, e in enumerate(line):
                details[j][e] += 1
    
    indices = sorted(details.keys())
    gamma_str = "".join([
        sorted([(k, v) for k, v in details[i].items()], key=lambda t: t[1])[-1][0] for i in indices
    ])
    epsilon_str = "".join([
        sorted([(k, v) for k, v in details[i].items()], key=lambda t: t[1])[0][0] for i in indices
    ])
    print(int(gamma_str, 2), int(epsilon_str, 2))
    return int(gamma_str, 2), int(epsilon_str, 2)
    

if __name__ == "__main__":
    gamma, epsilon = process(sys.argv[1])
    print(gamma * epsilon)

