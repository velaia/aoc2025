from pathlib import Path


def calculate_distance(file: Path) -> int:
    overall_dist = 0
    sources, dsts = [], []
    with Path(file).open() as sample:
        for line in sample.readlines():
            a, b = line.split()[0:2]
            sources.append(int(a))
            dsts.append(int(b))

        sources = sorted(sources)
        dsts = sorted(dsts)

        for i, val in enumerate(sources):
            overall_dist += abs(val - dsts[i])
    return overall_dist

def calculate_similarity(file: Path) -> int:
    overall = 0
    sources, dsts = [], []
    dst_counts = {}
    with Path(file).open() as sample:
        for line in sample.readlines():
            a, b = line.split()[0:2]
            sources.append(int(a))
            dsts.append(int(b))
    
    for dst in dsts:
        if dst in dst_counts:
            dst_counts[dst] += 1
        else:
            dst_counts[dst] = 1

    for src in sources:
        if src in dst_counts:
            overall += src * dst_counts[src]
    
    return overall


if __name__ == "__main__":
    sample_file = "2024/day1/sample1.txt"
    input_file = "2024/day1/input.txt"
    assert 11 == calculate_distance(sample_file)

    print(calculate_distance(input_file))

    # part 2 - similarity score
    assert 31 == calculate_similarity(sample_file)

    print(calculate_similarity(input_file))