from loader import load_strs


def find_repeat(rucksack):
    return (
        set(rucksack[: len(rucksack) // 2])
        .intersection(set(rucksack[len(rucksack) // 2 :]))
        .pop()
    )


def priority(item):
    return ord(item) - 96 if item.islower() else ord(item) - 38


def repeats(rucksacks):
    return sum(priority(find_repeat(rucksack)) for rucksack in rucksacks)


def find_badge(rucksacks):
    return (
        set(rucksacks[0])
        .intersection(set(rucksacks[1]))
        .intersection(set(rucksacks[2]))
        .pop()
    )


def badges(rucksacks):
    clusters = [rucksacks[3 * i : 3 * i + 3] for i in range(len(rucksacks) // 3)]
    return sum(priority(find_badge(cluster)) for cluster in clusters)


if __name__ == "__main__":
    rucksacks = load_strs("inputs/day03.txt")
    print(f"Part 1: {repeats(rucksacks)}")
    print(f"Part 2: {badges(rucksacks)}")


# -- Tests --

fixture = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]


def test_part_1():
    assert repeats(fixture) == 157


def test_part_2():
    assert badges(fixture) == 70
