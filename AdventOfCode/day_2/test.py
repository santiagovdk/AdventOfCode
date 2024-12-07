import unittest

from AdventOfCode.day_2.main import is_increasing, is_decreasing, is_report_safe


class IncreaseTestCase(unittest.TestCase):
    def test_returns_true_when_list_is_increasing(self):
        input_data = [1, 2, 3, 4, 5, 6]
        result = is_increasing(input_data)
        assert result == True

    def test_returns_false_when_list_is_not_increasing(self):
        input_data = [6, 5, 4, 3, 2, 1]
        result = is_increasing(input_data)
        assert result == False

        input_data = [1,2,3,10,11,12,13]
        result = is_increasing(input_data)
        assert result == False

    def test_returns_true_when_list_has_separation_of_more_than_3_once(self):
        input_data = [1, 2, 3, 4, 5, 6, 10]
        result = is_increasing(input_data)
        assert result == True

        input_data = [1, 2, 3, 10, 4, 5, 6]
        result = is_increasing(input_data)
        assert result == True

        input_data = [1, 10, 2, 3, 4, 5, 6]
        result = is_increasing(input_data)
        assert result == True

    def test_returns_false_when_list_has_separation_of_more_than_3_more_once(self):
        input_data = [1, 2, 9, 4, 5, 6, 10]
        result = is_increasing(input_data)
        assert result == False

        input_data = [1, 8, 3, 10, 4, 5, 6]
        result = is_increasing(input_data)
        assert result == False

        input_data = [1, 10, 2, 3, 4, 9, 6]
        result = is_increasing(input_data)
        assert result == False

    def test_returns_true_when_list_has_separation_of_less_than_1_once(self):
        input_data = [1, 1, 2, 3, 4, 5, 6]
        result = is_increasing(input_data)
        assert result == True

        input_data = [1, 2, 3, 3, 4, 5, 6]
        result = is_increasing(input_data)
        assert result == True

        input_data = [1, 2, 3, 4, 5, 6, 6]
        result = is_increasing(input_data)
        assert result == True

    def test_returns_false_when_list_has_separation_of_less_than_1_more_than_once(self):
        input_data = [1, 1, 2, 3, 3, 4, 5, 6]
        result = is_increasing(input_data)
        assert result == False

        input_data = [1, 2, 3, 3, 4, 5, 6, 6]
        result = is_increasing(input_data)
        assert result == False

        input_data = [1, 1, 2, 3, 4, 5, 6, 6]
        result = is_increasing(input_data)
        assert result == False


class DecreaseTestCase(unittest.TestCase):
    def test_returns_true_when_list_is_decreasing(self):
        input_data = [10, 9, 8, 7, 6, 5]
        result = is_decreasing(input_data)
        assert result == True

    def test_returns_false_when_list_is_not_decreasing(self):
        input_data = [1, 2, 3, 4, 5, 6]
        result = is_decreasing(input_data)
        assert result == False

    def test_returns_true_when_list_has_separation_of_more_than_3_once(self):
        input_data = [10, 9, 8, 7, 6, 5, 1]
        result = is_decreasing(input_data)
        assert result == True

        input_data = [10, 9, 8, 4, 3, 2, 1]
        result = is_decreasing(input_data)
        assert result == True

        input_data = [10, 6, 5, 4, 3, 2, 1]
        result = is_decreasing(input_data)
        assert result == True

    def test_returns_false_when_list_has_separation_of_more_than_3_more_than_once(self):
        input_data = [10, 2, 9, 8, 7, 6, 5, 1]
        result = is_decreasing(input_data)
        assert result == False

        input_data = [10, 1, 8, 4, 3, 2, 1]
        result = is_decreasing(input_data)
        assert result == False

        input_data = [10, 6, 5, 1, 3, 2, 1]
        result = is_decreasing(input_data)
        assert result == False

    def test_returns_true_when_list_has_separation_of_less_than_1_once(self):
        input_data = [10, 10, 9, 8, 7, 6, 5]
        result = is_decreasing(input_data)
        assert result == True

        input_data = [10, 9, 8, 8, 7, 6, 5]
        result = is_decreasing(input_data)
        assert result == True

        input_data = [10, 9, 8, 7, 6, 5, 5]
        result = is_decreasing(input_data)
        assert result == True

    def test_returns_false_when_list_has_separation_of_less_than_1_more_than_once(self):
        input_data = [10, 10, 9, 8, 7, 6, 5, 5]
        result = is_decreasing(input_data)
        assert result == False

        input_data = [10, 10, 9, 8, 8, 7, 6, 5]
        result = is_decreasing(input_data)
        assert result == False

        input_data = [10, 9, 9, 8, 7, 6, 5, 5]
        result = is_decreasing(input_data)
        assert result == False


class CheckSafeTestCase(unittest.TestCase):
    def test_unsafe_report_is_marked_as_unsafe(self):
        report = [1, 2, 7, 8, 9]
        result = is_report_safe(report)
        assert result == False


if __name__ == "__main__":
    unittest.main()
