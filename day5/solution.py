from pathlib import Path


def parse_file(file: Path) -> tuple:
    fresh_ranges: list = []
    ingredients: list[int] = []
    switched = False

    with file.open() as input:
        for line in input.readlines():
            if line.strip() == "":
                switched = True
                continue

            if switched is False:
                r = line.strip().split("-")
                fresh_ranges.append(r)
            else:
                i = line.strip()
                ingredients.append(i)

    return fresh_ranges, ingredients


def fresh_ingredients(fresh_ranges: list, ingredients: list) -> int:
    counter = 0
    inner_done = False

    for ing in ingredients:
        inner_done = False
        for ran in fresh_ranges:
            if int(ing) in range(int(ran[0]), int(ran[1]) + 1) and not inner_done:
                counter += 1
                inner_done = True
                # could break out of inner loop to improve perform.

    return counter

def num_fresh_ids(fresh_ranges: list) -> int:
    fresh_ids = set()

    for ran in fresh_ranges:
        start, stop = int(ran[0]), int(ran[1])
        for item in range(start, stop + 1):
            fresh_ids.add(item)

    return len(fresh_ids)

def num_fresh_ids2(fresh_ranges: list) -> int:
    merged = []
    overall = 0
    fresh_ranges = [[int(ran[0]), int(ran[1])] for ran in fresh_ranges]

    fresh_ranges.sort(key=lambda x: x[0])

    for i, ran in enumerate(fresh_ranges):
        if not merged or int(merged[-1][1]) < int(ran[0]):
            merged.append(ran)
        else:
            merged[-1][1] = max(int(merged[-1][1]), int(ran[1]))

    for mer in merged:
        overall += mer[1] - mer[0] +1
    
    return overall


if __name__ == "__main__":
    sample = Path("day5/sample.txt")
    input = Path("day5/input.txt")

    # sample assertion
    fresh_ranges, ingredients = parse_file(sample)
    num_fresh = fresh_ingredients(fresh_ranges, ingredients)
    assert 3 == num_fresh
    # part 2 sample
    num_fresh_ids_sample = num_fresh_ids(fresh_ranges)
    assert 14 == num_fresh_ids_sample
    num_fresh_ids_sample = num_fresh_ids2(fresh_ranges)
    assert 14 == num_fresh_ids_sample

    # input
    fresh_ranges, ingredients = parse_file(input)
    num_fresh = fresh_ingredients(fresh_ranges, ingredients)
    print(f"{num_fresh=}")
    # part 2 input
    num_fresh_ids_input = num_fresh_ids2(fresh_ranges)
    print(f"{num_fresh_ids_input=}")
