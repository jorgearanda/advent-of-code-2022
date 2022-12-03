from loader import load_strs


def round_score_first_approach(round):
    if round[2] == "X":
        score_for_move = 1
    elif round[2] == "Y":
        score_for_move = 2
    else:
        score_for_move = 3

    if round in {"B X", "C Y", "A Z"}:  # Defeats
        score_for_outcome = 0
    elif round in {"A X", "B Y", "C Z"}:  # Ties
        score_for_outcome = 3
    else:
        score_for_outcome = 6

    return score_for_move + score_for_outcome


def total_score_first_approach(rounds):
    return sum(round_score_first_approach(round) for round in rounds)


def round_score_second_approach(round):
    if round[2] == "X":
        score_for_outcome = 0
    elif round[2] == "Y":
        score_for_outcome = 3
    else:
        score_for_outcome = 6

    if round in {"A Y", "B X", "C Z"}:  # I must play Rock
        score_for_move = 1
    elif round in {"B Y", "C X", "A Z"}:  # I must play Paper
        score_for_move = 2
    else:  # Scissors it is
        score_for_move = 3
    return score_for_move + score_for_outcome


def total_score_second_approach(rounds):
    return sum(round_score_second_approach(round) for round in rounds)


if __name__ == "__main__":
    rounds = load_strs("inputs/day02.txt")

    print(f"Part 1: {total_score_first_approach(rounds)}")
    print(f"Part 2: {total_score_second_approach(rounds)}")


# -- Tests --
fixture = ["A Y", "B X", "C Z"]


def test_part_1():
    assert total_score_first_approach(fixture) == 15


def test_part_2():
    assert total_score_second_approach(fixture) == 12
