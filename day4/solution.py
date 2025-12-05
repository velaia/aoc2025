from pathlib import Path
import numpy as np

PAPER = "@"


def check_env(cell_row, cell_col, map) -> int:
    num_papers: int = -1  # cell itself is tested, so subtract 1

    for i in range(cell_row - 1, cell_row + 2):
        for j in range(cell_col - 1, cell_col + 2):
            if i >= 0 and j >= 0:
                try:
                    cell_value = map[i][j]
                    if cell_value == PAPER:
                        num_papers += 1
                except IndexError:
                    pass  # no paper outside of map boundaries

    return num_papers


def num_papers_that_can_be_removed(map: list[str]) -> list[int, list]:
    solution: int = 0
    new_map = map.copy()
    for i, row in enumerate(map):
        new_map[i] = map[i].copy()
        for j, cell in enumerate(row):
            if cell == PAPER:
                if check_env(i, j, map) < 4:
                    solution += 1
                    new_map[i][j] = "."
    return [solution, new_map]


def check_file(file: Path) -> int:
    with Path(file).open() as sample:
        map: list[list[str]] = []

        for line in sample.readlines():
            map.append([str(ch) for ch in line.strip()])

        return num_papers_that_can_be_removed(map)[0]


def check_file2(file: Path) -> int:
    with Path(file).open() as sample:
        map: list[list[str]] = []

        for line in sample.readlines():
            map.append([str(ch) for ch in line.strip()])

        num_overall: int = 0
        num_changed, new_map = num_papers_that_can_be_removed(map)
        num_overall += num_changed
        while num_changed > 0:
            num_changed, new_map = num_papers_that_can_be_removed(new_map)
            num_overall += num_changed

        return num_overall


if __name__ == "__main__":
    solution = check_file(Path("day4/sample1.txt"))
    assert 13 == solution

    print(f"part 1: {check_file("day4/input1.txt")}")

    # part 2
    solution2 = check_file2(Path("day4/sample1.txt"))
    assert 43 == solution2

    print(f"part 2: { check_file2(Path("day4/input1.txt"))}")
