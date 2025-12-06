from pathlib import Path
from functools import reduce


def solve_sheet(path: str) -> int:
    overall:int = 0
    with Path(path).open() as sheet:
        table = []
        for line in sheet.readlines():
            values = line.strip().split()
            table.append(values)
        
        # iterate over table cols
        rows = len(table)
        cols = len(table[0])
        for i in range(cols):
            parts = [table[row][i] for row in range(rows - 1)]

            action = table[rows-1][i]
            if action == "*":
                overall += reduce(lambda x, y: x * y, [int(part) for part in parts])
            else:
                overall += reduce(lambda x, y: x + y, [int(part) for part in parts])

    return overall


def reformat(parts: list[str]) -> list[int]:
    result: list[int] = []
    max_len = len(parts[0])

    vertical_nums = []
    for i in range(max_len):
        nums = [parts[j][i] for j in range(len(parts))]
        vertical_nums.append(nums)

    result = [int("".join(res).replace("0", "")) for res in vertical_nums]
    return result


def solve_part2(path: str) -> int:
    overall = 0

    with Path(path).open() as sheet:
        table = []
        lines = []
        for line in sheet.readlines():
            values = line.strip().split()
            table.append(values)
            lines.append(line)

        # iterate over table cols
        offset = 0
        rows = len(table)
        cols = len(table[0])
        for i in range(cols):
            parts = [table[row][i] for row in range(rows - 1)]
            max_len = max([len(part) for part in parts])
            new_parts = [lines[row][offset:offset+max_len] for row in range(rows-1)]
            new_parts = [part.replace(" ", "0") for part in new_parts]
            action = table[rows-1][i]

            new_parts = reformat(new_parts)

            if action == "*":
                overall += reduce(lambda x, y: x * y, [part for part in new_parts])
            else:
                overall += reduce(lambda x, y: x + y, [part for part in new_parts])
            
            offset += max_len + 1

    return overall


if __name__ == "__main__":
    sample = "day6/sample.txt"
    input = "day6/input.txt"

    sample_solution = solve_sheet(sample)
    assert 4277556 == sample_solution

    input_solution = solve_sheet(input)
    print(f"{input_solution=}")

    # part 2
    # test reformat
    reformated = reformat(["0003", "0075", "0459", "3222"])
    assert 3592 in reformated
    assert 3 in reformated

    sample_solution = solve_part2(sample)
    assert 3263827 == sample_solution

    input_solution = solve_part2(input)
    print(f"{input_solution=}")