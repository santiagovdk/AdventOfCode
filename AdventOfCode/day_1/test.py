import unittest

from AdventOfCode.day_1.part_1 import (
    parse_data_line,
    get_distance_between_first_numbers,
    get_total_distance_between_lists,
)


class LookupTestCase(unittest.TestCase):

    def test_parse_data_line(self):
        input_data = "12345   67890"
        result = parse_data_line(input_data)
        assert result == [12345, 67890]

    def test_get_distance_between_first_numbers(self):
        left_list = [3, 4, 2, 1, 3, 3]
        right_list = [4, 3, 5, 3, 9, 3]
        result = get_distance_between_first_numbers(left_list, right_list)
        assert result == 1

    def test_get_total_distance_between_lists(self):
        left_list = [1, 2]
        right_list = [4, 3]
        result = get_total_distance_between_lists(left_list, right_list)
        assert result == 4


if __name__ == "__main__":
    unittest.main()
