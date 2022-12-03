from loader import load_int_chunks


def calories_per_elf(elves):
    return sorted([sum(elf) for elf in elves], reverse=True)


def most_calories(elves):
    return calories_per_elf(elves)[0]


def top_three(elves):
    return sum(calories_per_elf(elves)[:3])


if __name__ == "__main__":
    elves = load_int_chunks("inputs/day01.txt")

    print(f"Part 1: {most_calories(elves)}")
    print(f"Part 2: {top_three(elves)}")


# -- Tests --
fixture = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]


def test_part_1():
    assert most_calories(fixture) == 24000


def test_part_2():
    assert top_three(fixture) == 45000
