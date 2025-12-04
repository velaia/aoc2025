from pathlib import Path

def is_invalid(id: int) -> bool:
    id = str(id)
    if id[:len(id)//2] == id[len(id)//2:]:
        return True
    return False

def find_invalid_ids(file: Path) -> list[int]:
    solution = []

    # get ranges
    ranges = []
    with file.open() as sample:
        for line in sample.readlines():
            ranges.extend(line.strip()[:-1].split(","))
    
    for ran in ranges:
        lower, upper = ran.split("-")
        for i in range(int(lower), int(upper) + 1):
            if is_invalid(i):
                solution.append(i)

    return solution

if __name__ == "__main__":
    solution: int = 0

    assert is_invalid(123123) is True
    assert is_invalid(123456) is False

    solution = sum(find_invalid_ids(Path("day2/sample1.txt")))

    assert solution == 1227775554

    solution2 = sum(find_invalid_ids(Path("day2/input1.txt")))
    print(f"day 2 p 1: {solution2}")
    
