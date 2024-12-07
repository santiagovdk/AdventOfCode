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
        # raise ValueError(f"{report} is not increasing or decreasing")


def is_increasing(report: t.List[int], problem_dampener=False) -> bool:
    i = 0
    is_problem_dampener_engaged = not problem_dampener
    while i < len(report) - 1:
        current_value = report[i]
        next_value = report[i + 1]

        try:
            if next_value <= current_value:
                raise ValueError(f"Next value is not increasing, {current_value} -> {next_value}")
                # return False
            elif abs(current_value - next_value) > 3:
                raise ValueError(f"Next value is increasing by more than three, {current_value} -> {next_value}")
                # return False
            else:
                i += 1
        except ValueError as e:
            print(e)
            if is_problem_dampener_engaged:
                return False
            else:
                is_problem_dampener_engaged = True
                i += 1
                continue

    return True


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
