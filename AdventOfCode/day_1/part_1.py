from pathlib import Path
import typing as t
import sys

# Number of elements + 3
sys.setrecursionlimit(1003)

SEPARATOR = "   "


def parse_data_line(line: str) -> t.List[int]:
    return [int(number) for number in line.strip().split(SEPARATOR)]


def get_distance_between_first_numbers(
    left_list: t.List[int], right_list: t.List[int]
) -> int:
    smallest_left_number = left_list.pop(0)
    smallest_right_number = right_list.pop(0)
    return abs(smallest_left_number - smallest_right_number)


def get_total_distance_between_lists(
    left_list: t.List[int],
    right_list: t.List[int],
    result=0,
) -> int:
    result += get_distance_between_first_numbers(left_list, right_list)
    if len(left_list) == 0 or len(right_list) == 0:
        return result
    return get_total_distance_between_lists(left_list, right_list, result)


if __name__ == "__main__":
    left_list: t.List[int] = []
    right_list: t.List[int] = []
    file = Path("data_input.txt")
    with file.open("r") as fd:
        for line in fd:
            parsed_line = parse_data_line(line)
            left_list.append(parsed_line[0])
            right_list.append(parsed_line[1])

    left_list.sort()
    right_list.sort()
    print(f"Result: {get_total_distance_between_lists(left_list, right_list)}")
    # Answer: 1879048
