from pathlib import Path
import re

def is_invalid(id: int) -> bool:
    id = str(id)
    if id[:len(id)//2] == id[len(id)//2:]:
        return True
    return False

def is_invalid2(id: int) -> bool:
    if id == 2121212121:
        ...
    id_len = len(str(id))
    for i in range(1, id_len//2 + 1):
        p = re.compile("(" + str(id)[:i] + "){" + str(id_len // i) + "}")
        if p.match(str(id)):
            if i * (id_len // i) == id_len:
                return True
    return False


def find_invalid_ids(file: Path, fn) -> list[int]:
    solution = []

    # get ranges
    ranges = []
    with file.open() as sample:
        for line in sample.readlines():
            ranges.extend(line.strip()[:-1].split(","))
    
    for ran in ranges:
        lower, upper = ran.split("-")
        for i in range(int(lower), int(upper) + 1):
            if fn(i):
                solution.append(i)

    return solution

if __name__ == "__main__":
    solution: int = 0

    assert is_invalid(123123) is True
    assert is_invalid(123456) is False

    solution = sum(find_invalid_ids(Path("day2/sample1.txt"), is_invalid))

    assert solution == 1227775554

    solution2 = sum(find_invalid_ids(Path("day2/input1.txt"), is_invalid))
    print(f"day 2 p 1: {solution2}")

    # part 2
    assert is_invalid2(121212) is True
    assert is_invalid2(1212) is True
    assert is_invalid2(12123) is False
    assert is_invalid2(32323232323232) is True

    invalid_ids = find_invalid_ids(Path("day2/sample1.txt"), is_invalid2)
    solution4 = sum(invalid_ids)
    assert 4174379265 == solution4
    
    solution3 = sum(find_invalid_ids(Path("day2/input1.txt"), is_invalid2))
    print(f"day 2 p 2: {solution3}")
