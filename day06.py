from loader import load_strs


def distinct(buffer, amount):
    """
    Report the character *after* the first substring of length _amount_
    that consists of only distinct characters.
    """
    for i in range(amount, len(buffer)):
        if len(set(list(buffer[i - amount : i]))) == amount:
            return i


def start_marker(buffer):
    return distinct(buffer, 4)


def start_message_marker(buffer):
    return distinct(buffer, 14)


if __name__ == "__main__":
    buffer = load_strs("inputs/day06.txt")[0]
    print(f"Part 1: {start_marker(buffer)}")
    print(f"Part 2: {start_message_marker(buffer)}")


## -- Tests --

fix1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"


def test_part_1():
    assert start_marker(fix1) == 7


def test_part_2():
    assert start_message_marker(fix1) == 19
