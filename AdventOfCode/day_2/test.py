import unittest

from AdventOfCode.day_2.main import is_increasing, is_decreasing, is_report_safe

class IncreaseWithProblemDampenerTestCase(unittest.TestCase):
    def test_returns_true_when_list_is_increasing_by_more_than_3_units_with_problem_dampener(self):
        # Middle
        input_data = [1, 2, 3, 4, 11, 5, 6]
        result = is_increasing(input_data, problem_dampener=True)
        assert result == True

        # Start
        input_data = [1, 11, 2, 3, 4, 5]
        result = is_increasing(input_data, problem_dampener=True)
        assert result == True

        # End
        input_data = [1, 2, 3, 4, 5, 6, 12]
        result = is_increasing(input_data, problem_dampener=True)
        assert result == True

    def test_returns_true_when_list_is_increasing_by_less_than_1_units_with_problem_dampener(self):
        # Middle
        input_data = [1, 2, 3, 4, 5, 5, 6, 7]
        result = is_increasing(input_data, problem_dampener=True)
        assert result == True

        # Start
        input_data = [1, 1, 2, 3, 4, 5, 6, 7]
        result = is_increasing(input_data, problem_dampener=True)
        assert result == True

        # End
        input_data = [1, 2, 3, 4, 5, 6, 7, 7]
        result = is_increasing(input_data, problem_dampener=True)
        assert result == True

class IncreaseTestCase(unittest.TestCase):
    def test_returns_true_when_list_is_increasing(self):
        input_data = [1, 2, 3, 4, 5, 6]
        result = is_increasing(input_data)
        assert result == True

    def test_returns_false_when_list_is_not_increasing(self):
        input_data = [6, 5, 4, 3, 2, 1]
        result = is_increasing(input_data)
        assert result == False

    def test_returns_false_when_list_is_increasing_by_more_than_3_units(self):
        # Middle
        input_data = [1, 2, 3, 4, 11, 5, 6]
        result = is_increasing(input_data)
        assert result == False

        # Start
        input_data = [1, 11, 2, 3, 4, 5]
        result = is_increasing(input_data)
        assert result == False

        # End
        input_data = [1, 2, 3, 4, 5, 6, 12]
        result = is_increasing(input_data)
        assert result == False

    def test_returns_false_when_list_is_increasing_by_less_than_1_units(self):
        # Middle
        input_data = [1, 2, 3, 4, 5, 5, 6, 7]
        result = is_increasing(input_data)
        assert result == False

        # Start
        input_data = [1, 1, 2, 3, 4, 5, 6, 7]
        result = is_increasing(input_data)
        assert result == False

        # End
        input_data = [1, 2, 3, 4, 5, 6, 7, 7]
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

    def test_returns_false_when_list_is_decreasing_by_more_than_3_units(self):
        # Middle
        input_data = [15, 14, 13, 12, 6, 11, 10, 9]
        result = is_decreasing(input_data)
        assert result == False

        # Start
        input_data = [15, 6, 14, 13, 12, 11, 10]
        result = is_decreasing(input_data)
        assert result == False

        # End
        input_data = [15, 14, 13, 12, 11, 10, 3]
        result = is_decreasing(input_data)
        assert result == False

    def test_returns_false_when_list_is_decreasing_by_less_than_1_units(self):
        # Middle
        input_data = [15, 14, 13, 12, 11, 11, 10, 9]
        result = is_decreasing(input_data)
        assert result == False

        # Start
        input_data = [15, 15, 14, 13, 12, 11, 10, 9]
        result = is_decreasing(input_data)
        assert result == False

        # End
        input_data = [15, 14, 13, 12, 11, 10, 9, 9]
        result = is_decreasing(input_data)
        assert result == False

class CheckSafeTestCase(unittest.TestCase):
    def test_unsafe_report_is_marked_as_unsafe(self):
        report = [1, 2, 7, 8, 9]
        result = is_report_safe(report)
        assert result == False


if __name__ == "__main__":
    unittest.main()
