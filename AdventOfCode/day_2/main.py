from pathlib import Path
import typing as t

SEPARATOR = " "


def parse_data_line(line: str) -> t.List[int]:
    return [int(number) for number in line.strip().split(SEPARATOR)]


# The cadence is determine from left to right
def is_report_safe(report: t.List[int]) -> bool:
    if is_increasing(report, problem_dampener=True):
        return True
    elif is_decreasing(report, problem_dampener=True):
        return True
    else:
        return False


def is_increasing(report: t.List[int], problem_dampener=False) -> bool:
    is_safe = True

    current_value_index = 0
    next_value_index = 1

    is_problem_dampener_engaged = not problem_dampener
    dampening_problem = False

    while current_value_index < len(report) - 1:
        if problem_dampener is True and next_value_index == len(report) - 1:
            break

        try:
            current_value = report[current_value_index]
            next_value = report[next_value_index]

            if next_value <= current_value:
                raise ValueError(f"Next value is not increasing, {current_value} -> {next_value}")
            elif abs(current_value - next_value) > 3:
                raise ValueError(f"Next value is increasing by more than three, {current_value} -> {next_value}")
            elif dampening_problem and problem_dampener:
                # Recently engaged problem dampener
                current_value_index = next_value_index
                next_value_index += 1
            else:
                # Safe
                current_value_index += 1
                next_value_index += 1
        except ValueError as e:
            if problem_dampener:
                if is_problem_dampener_engaged:
                    is_safe = False
                    break
                else:
                    is_problem_dampener_engaged = True
                    dampening_problem = True
                    next_value_index += 1
                    continue

            is_safe = False
            break

    return is_safe


def is_decreasing(report: t.List[int]) -> bool:
    i = 0
    while i < len(report) - 1:
        current_value = report[i]
        next_value = report[i + 1]

        if next_value >= current_value:
                return False
        else:
            if abs(current_value - next_value) > 3:
                    return False
            i += 1
    return True


if __name__ == "__main__":
    file = Path("data_input.txt")
    safe_reports = 0
    with file.open("r") as fd:
        for line in fd:
            parsed_line = parse_data_line(line)
            report_result = is_report_safe(parsed_line)
            print(f"Is {parsed_line} safe? {report_result}")
            if report_result is True:
                safe_reports += 1

    print(f"Number of safe reports: {safe_reports}")
    # Answer part 1: 407
    # Answer part 2:
    # Not 458 *
    # Not 455 *
    # Not 515
    # Not 503
    # Not 508
    # 499?
