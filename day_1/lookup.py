import io
from pathlib import Path
import typing as t
import sys

# Number of elements + 3
sys.setrecursionlimit(1003)

SEPARATOR = "   "


def pop_smallest_number(numbers: t.List[int]) -> int:
    return numbers.pop(0)


def parse_data_line(line: str) -> t.List[int]:
    parsed_line = [int(number) for number in line.strip().split(SEPARATOR)]
    return parsed_line


def get_distance_between_smallest_numbers(
    left_list: t.List[int], right_list: t.List[int]
) -> int:
    smallest_left_number = pop_smallest_number(left_list)
    smallest_right_number = pop_smallest_number(right_list)
    return abs(smallest_left_number - smallest_right_number)


def get_total_distance_between_lists(
    left_list: t.List[int],
    right_list: t.List[int],
    result=0,
) -> int:
    result += get_distance_between_smallest_numbers(left_list, right_list)
    if len(left_list) == 0 or len(right_list) == 0:
        return result
    return get_total_distance_between_lists(left_list, right_list, result)


if __name__ == "__main__":
    left_list: t.List[int] = []
    right_list: t.List[int] = []
    file = Path(__file__).with_name("day_1_input.txt")
    with file.open("r") as fd:
        for line in fd:
            parsed_line = parse_data_line(line)
            left_list.append(parsed_line[0])
            right_list.append(parsed_line[1])

    left_list.sort()
    right_list.sort()
    print(get_total_distance_between_lists(left_list, right_list))
    # Answer: 1879048
