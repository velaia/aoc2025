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
            processed_row[i-1] = "|"
            processed_row[i+1] = "|"
            processed_row[i] = "^"

    processed_row = "".join(processed_row)
    return str(processed_row), num_splits


def calculate_split_count(path) -> int:
    file = Path(path)
    result = 0

    chart = []
    new_chart = []
    with file.open() as input_file:
        for line in input_file.readlines():
            chart.append(line.strip())
        
        processed_row = chart[0]
        for row in range(1, len(chart)):
            processed_row, splits = process_row(processed_row, chart[row])
            result += splits
            
            new_chart.append([ch for ch in processed_row])

        print(new_chart)

    
    return result


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