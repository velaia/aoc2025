from pathlib import Path

START: int = 50

class Dial:
    def __init__(self, start):
        self.position = start
        self.zeros_hit = 0
        self.zeros_pointed_at = 0

    def dial(self, direction: str, amount: int) -> None:
        assert direction in ('L', 'R')
        amount = int(amount)
        num_crossed = 0
        if direction == "L":
            for i in range(amount):
                self.position = (self.position - 1) % 100
                if self.position == 0:
                    num_crossed += 1
        elif direction == "R":
            for i in range(amount):
                self.position = (self.position + 1) % 100
                if self.position == 0:
                    num_crossed += 1
        self.zeros_pointed_at += num_crossed

        print(f"{direction}{amount}: {num_crossed=}, {self.zeros_pointed_at=}")

    
    def dial2(self, direction: str, amount: int) -> None:
        assert direction in ('L', 'R')
        amount = int(amount)
        num_crossed = 0
        if direction == 'L' and amount == 382:
            ...
        if direction == "L":
            self.new_position = self.position - amount
            if self.new_position <= 0:
                if self.new_position == 0:
                    num_crossed = 1
                elif self.new_position >= -100 and self.position == 0:
                    num_crossed = 0
                elif self.new_position < -100 and self.position != 0 and self.new_position % 100 ==0:
                    num_crossed = amount // 100 + 1
                elif self.new_position < -100 and self.position != 0:
                    num_crossed = amount // 100
                else:
                    num_crossed = amount // 100 + 1
            self.zeros_pointed_at += num_crossed
        elif direction == "R":
            self.new_position = self.position + amount
            if self.new_position / 100 >= 1.0:
                num_crossed = self.new_position // 100
                self.zeros_pointed_at += num_crossed

        # if self.position == 0 and self.new_position % 100 == 0:
        print(f"{direction}{amount}: {num_crossed=}, {self.zeros_pointed_at=}")
        self.position = self.new_position % 100
        if self.position == 0:
            self.zeros_hit += 1
    
    def get_zeros_hit(self) -> int:
        return self.zeros_hit
    
    def get_zeros_crossed(self) -> int:
        return self.zeros_pointed_at


    

def calc_zeros1(path: Path) -> int:
    # part 1
    dial1 = Dial(START)

    with path.open() as sample:
        for line in sample.readlines():
            direction, amount = line[0], line[1:].strip()

            dial1.dial(direction, amount)


    return dial1.get_zeros_hit(), dial1.get_zeros_crossed()
    



if __name__ == "__main__":
    # solution1 = calc_zeros1(Path("day1/sample.txt"))[0]
    # assert 3 == solution1

    # solution2 = calc_zeros1(Path("day1/input.txt"))[0]
    # print(f"part 1: {solution2}")

    # solution3 = calc_zeros1(Path("day1/sample.txt"))[1]
    # print(solution3)
    # assert 6 == solution3

    # solution6 = calc_zeros1(Path("day1/sample2.txt"))[1]
    # print(solution6)
    # assert 8 == solution6

    # solution5 = calc_zeros1(Path("day1/sample3.txt"))[1]
    # print(solution5)
    # assert 8 == solution5

    solution4 = calc_zeros1(Path("day1/input.txt"))[1]
    print(f"part 2: {int(solution4)}")

    