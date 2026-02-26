from pathlib import Path


def process_row(row1: str, row2: str):
    """
    .......|.......
    ......|^|......
    ......|.|......
    ......|^|......
    ......|.|......

    only split at ^ and if there's a | above

    """
    processed_row: list[str] = ["."] * len(row1)
    num_splits = 0

    for i, char in enumerate(row1):
        if char in ["|", "S"] and row2[i] != "^":
            processed_row[i] = "|"
        elif char in ["|", "S"] and row2[i] == "^":
            num_splits += 1
            processed_row[i - 1] = "|"
            processed_row[i + 1] = "|"
            processed_row[i] = "^"

    processed_row = "".join(processed_row)
    return str(processed_row), num_splits


def calculate_split_count(path) -> int:
    result = 0

    with Path(path).open() as input_file:
        chart = [line.strip() for line in input_file]

        processed_row = chart[0]
        for row in range(1, len(chart)):
            processed_row, splits = process_row(processed_row, chart[row])
            result += splits

    return result


def calculate_paths(path) -> int:
    with Path(path).open() as file:
        lines = [line.strip() for line in file]
        width = len(lines[0])
        values = [0] * width

        for line in lines:
            s_pos = line.find("S")
            if s_pos > 0:
                values[s_pos] = 1

            if line.find("^") != -1:
                for i, ch in enumerate(line):
                    if ch == "^":
                        values[i - 1] += values[i]
                        values[i + 1] += values[i]
                        values[i] = 0

        return sum(values)


if __name__ == "__main__":
    sample = "day7/sample.txt"
    target_sample_result = 21
    input = "day7/input.txt"

    # test row processor
    assert ("......|^|......", 1) == process_row(".......|.......", ".......^.......")
    assert (".......|.......", 0) == process_row(".......S.......", "...............")
    assert ("...|.|.|||.|...", 0) == process_row("...|^|^|||^|...", "...............")
    assert ("..|^|^|||^|^|..", 4) == process_row("...|.|.|||.|...", "...^.^...^.^...")

    sample_result = calculate_split_count(sample)
    assert target_sample_result == sample_result

    print(f"part 1: {calculate_split_count(input)}")

    # part 2 - logic from visualization under https://www.reddit.com/r/adventofcode/comments/1pgbg8a/2025_day_7_part_2_visualization_for_the_sample/
    target_path_count = 40
    sample_result = calculate_paths(sample)
    assert target_path_count == sample_result

    print(f"part 2: {calculate_paths(input)}")
