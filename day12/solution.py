from pathlib import Path


def read_file(path:str) -> list[str]:
    lines = []
    with Path(path).open() as input:
        for line in input.readlines():
            lines.append(line.strip())
    return lines


if __name__ == "__main__":
    dir = "day12"

    input_pattern_counts = [5, 7, 7, 7, 7, 6]
    lines = read_file("day12/input_p2")
    num_space_sufficient = 0
    for line in lines:
        x = int(line[0:2])
        y = int(line[3:5])
        counters = [int(counter) for counter in line[7:].split()]
        overall = 0
        for num1, num2 in zip(input_pattern_counts, counters):
            overall += num1*num2

        if x*y < overall:
            print("space not sufficient")
        else:
            print(f"available space: {x*y}, used by patterns: {overall}")
            num_space_sufficient += 1

            # continue calculation
            ...
    
    print(f"spaces with possibly sufficient space: {num_space_sufficient}")

    

    
