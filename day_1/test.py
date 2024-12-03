import unittest

from day_1.lookup import (
    pop_smallest_number,
    parse_data_line,
    get_distance_between_smallest_numbers,
    get_total_distance_between_lists,
)


class LookupTestCase(unittest.TestCase):
    def test_pop_smallest_number(self):
        numbers = [9, 3, 0, 7]
        result = pop_smallest_number(numbers)
        assert result == 0

    def test_parse_data_line(self):
        input_data = "12345   67890"
        result = parse_data_line(input_data)
        assert result == [12345, 67890]

    def test_get_distance_between_smallest_numbers(self):
        left_list = [3, 4, 2, 1, 3, 3]
        right_list = [4, 3, 5, 3, 9, 3]
        result = get_distance_between_smallest_numbers(left_list, right_list)
        assert result == 2

    def test_get_total_distance_between_lists(self):
        left_list = [3, 4, 2, 1, 3, 3]
        right_list = [4, 3, 5, 3, 9, 3]
        result = get_total_distance_between_lists(left_list, right_list)
        assert result == 11


if __name__ == "__main__":
    unittest.main()
