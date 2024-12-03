from pathlib import Path
import typing as t
import sys

SEPARATOR = "   "


def parse_data_line(line: str) -> t.List[int]:
    return [int(number) for number in line.strip().split(SEPARATOR)]


if __name__ == "__main__":
    left_list: t.List[int] = []
    right_list: t.List[int] = []
    file = Path("data_input.txt")
    with file.open("r") as fd:
        for line in fd:
            parsed_line = parse_data_line(line)
            left_list.append(parsed_line[0])
            right_list.append(parsed_line[1])

    score = 0
    for value in left_list:
        appearances = right_list.count(value)
        score += value * appearances
    print(f"Result: {score}")
    # Result 21024792
