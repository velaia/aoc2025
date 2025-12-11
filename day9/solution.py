from pathlib import Path
from matplotlib import pyplot as plt


def find_largest_rectanlge(path: str) -> int:
    tiles: list[tuple[int]] = []

    with Path("day9/" + path).open() as file:
        for line in file.readlines():
            tiles.append(line.strip().split(","))

    largest: int = 0
    
    for first in tiles:
        for second in tiles:
            area = abs(
                (int(first[0]) - int(second[0]) + 1) * 
                (int(first[1]) - int(second[1]) + 1))
            if area > largest:
                largest = area

    return largest


if __name__ == "__main__":
    dir = "day8"

    for path in ("sample", "input"):
        result = find_largest_rectanlge(path)
        if path == "sample":
            assert 50 == result

        print(f"{path}: {result}")

        # part 2
    