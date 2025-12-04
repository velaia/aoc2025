import os
from pathlib import Path

def largest_joltage(bank: str) -> int:
    bank = bank.strip()
    nums = [int(num) for num in bank]
    largest: int = 0
    largest_pos: int = 0
    for i, num in enumerate(nums[:-1]):
        if num > largest:
            largest = num
            largest_pos = i
    second_part = sorted(nums[largest_pos+1:])[-1]
    return largest * 10 + second_part

def largest_joltage2(bank: str) -> int:
    solution_nums: list[int] = []
    num_length: int = 12
    begin_index: int = 0
    nums = [int(num) for num in bank.strip()]
    for i in range(num_length, 0, -1):
        valid_range = nums[begin_index:len(nums) - i + 1]
        largest: int = 0
        largest_pos: int = 0
        for j, num in enumerate(valid_range):
            if num > largest:
                largest = num
                largest_pos = j
        solution_nums.append(largest)
        largest = 0
        begin_index += largest_pos + 1
        ...
    return "".join([str(num) for num in solution_nums])



if __name__ == "__main__":
    with Path("day3/sample1.txt").open() as sample:
        sample_sum: int = 0
        for bank in sample.readlines():
            sample_sum += largest_joltage(bank)
        assert 357 == sample_sum


    with Path("day3/sample1.txt").open() as sample:
        # part 2
        sample_sum2: int = 0
        # test largest_joltage2:
        assert "434234234278" == largest_joltage2("234234234234278")
        for bank in sample:
            sample_sum2 += int(largest_joltage2(bank))

        assert 3121910778619 == sample_sum2

    with Path("day3/input1.txt").open() as input:
        sum: int = 0
        for bank in input.readlines():
            sum += largest_joltage(bank)
        print(f"part1: {sum}")

    with Path("day3/input1.txt").open() as input:
        # part 2
        sum2: int = 0
        # test largest_joltage2:
        for bank in input:
            sum2 += int(largest_joltage2(bank))
        print(f"part2: {sum2}")