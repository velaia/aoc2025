from pathlib import Path
import numpy as np

PAPER = "@"

def check_env(cell_row, cell_col, map) -> int:
    num_papers: int = -1 # cell itself is tested, so subtract 1

    for i in range(cell_row - 1, cell_row + 2):
        for j in range(cell_col - 1, cell_col + 2):
            if i >= 0 and j >= 0:
                try:
                    cell_value = map[i][j]
                    if cell_value == PAPER:
                        num_papers += 1
                except IndexError:
                    pass # no paper outside of map boundaries
    
    return num_papers


def check_file(file: Path) -> int:
    with Path(file).open() as sample:
        solution: int = 0
        map: list[str] = []

        for line in sample.readlines():
            map.append(line.strip())
        
        for i, row in enumerate(map):
            for j, cell in enumerate(row):
                if cell == PAPER:
                    if check_env(i, j, map) < 4:
                        solution += 1
    return solution

if __name__ == "__main__":
        solution = check_file(Path("day4/sample1.txt"))
        assert 13 == solution

        print(f"part 1: {check_file("day4/input1.txt")}")
