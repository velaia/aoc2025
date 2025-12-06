from pathlib import Path


def get_trails_for_pos_val(pos, val: int, map:list[str]):
    # top
    if pos[0] == 0:
        top = None
    else:
        top = map[pos[0] - 1][pos[1]]
    if top and val != 9:
        return get_trails_for_pos_val((pos[0] -1, pos[1]), val+1, map)
    elif top and val == 9:
        return ((pos[0] - 1, pos[1]))

    # right
    if pos[1] == len(map[0]) - 1:
        right = None
    else:
        right = map[pos[0]][pos[1] + 1]

    # bottom
    if pos[0] == len(map) - 1:
        bottom = None
    else:
        bottom = map[pos[0] + 1][pos[1]]

    # left
    if pos[1] == 0:
        left = None
    else:
        left = map[pos[0]][pos[1] - 1]



def get_trailhead_scores(file: Path) -> int:
    map = []
    results = []
    with file.open() as input:
        for line in input.readlines():
            map.append(line.strip())
    
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if int(cell) == 0:
                print(f"possible start: {i, j =}")
                results.append(get_trails_for_pos_val((i, j), 1, map))
    
    print(results)




if __name__ == "__main__":
    sample = Path("2024/day10/sample.txt")
    input = Path("2024/day10/sample.txt")

    sample_scores = get_trailhead_scores(sample)