from loader import load_strs


def parse_assignment_pairs(ap):
    return [
        [int(limit) for limit in assignment.split("-")] for assignment in ap.split(",")
    ]


def enclosed(ranges):
    start1, end1 = ranges[0]
    start2, end2 = ranges[1]
    return (start2 <= start1 <= end1 <= end2) or (start1 <= start2 <= end2 <= end1)


def enclosed_sum(assignment_pairs):
    return sum(enclosed(parse_assignment_pairs(ap)) for ap in assignment_pairs)


def overlap(ranges):
    start1, end1 = ranges[0]
    start2, end2 = ranges[1]
    return end1 >= start2 and end2 >= start1


def overlap_sum(assignment_pairs):
    return sum(overlap(parse_assignment_pairs(ap)) for ap in assignment_pairs)


if __name__ == "__main__":
    aps = load_strs("inputs/day04.txt")
    print(f"Part 1: {enclosed_sum(aps)}")
    print(f"Part 2: {overlap_sum(aps)}")


# --Tests--

fixture = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8",
]


def test_parse():
    assert parse_assignment_pairs("2-4,6-8") == [[2, 4], [6, 8]]


def test_part_1():
    assert enclosed_sum(fixture) == 2


def test_part_2():
    assert overlap_sum(fixture) == 4
