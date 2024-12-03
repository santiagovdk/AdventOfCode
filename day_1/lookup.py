import io
from pathlib import Path
import typing as t

SEPARATOR = "   "


def pop_smallest_number(numbers: t.List[int]) -> int:
    numbers.sort()
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


def __main__():
    input_data = []
    with io.open(Path("./day-1-input.txt")) as fd:
        input_data.append(parse_data_line(fd.readline()))
