from dataclasses import dataclass

from loader import load_strs


@dataclass
class Move:
    quantity: int
    source: int
    target: int


def parse_input(lines):
    stack_lines = []
    move_lines = []
    on_stack = True
    for line in lines:
        if line == "":
            on_stack = False
            continue
        if on_stack:
            stack_lines.append(line)
        else:
            move_lines.append(line)

    return parse_stacks(stack_lines), parse_moves(move_lines)


def parse_stacks(lines):
    stacks = {}
    stack = None
    for i in range(1, len(lines[-1]), 4):
        for line in lines[::-1]:
            if line[i].isdigit():
                stack = int(line[i])
                stacks[stack] = []
            elif line[i] == " ":
                continue
            else:
                stacks[stack].append(line[i])
    return stacks


def parse_moves(lines):
    moves = []
    for line in lines:
        tokens = line.split()
        moves.append(Move(int(tokens[1]), int(tokens[3]), int(tokens[5])))
    return moves


def run_9000(stacks, moves):
    for move in moves:
        for _ in range(move.quantity):
            stacks[move.target].append(stacks[move.source].pop())
    return stacks


def run_9001(stacks, moves):
    for move in moves:
        stacks[move.target] = (
            stacks[move.target]
            + stacks[move.source][len(stacks[move.source]) - move.quantity :]
        )
        stacks[move.source] = stacks[move.source][
            : len(stacks[move.source]) - move.quantity
        ]
    return stacks


def message(stacks):
    return "".join(stacks[stack][-1] for stack in stacks if len(stacks[stack]) > 0)


if __name__ == "__main__":
    stacks, moves = parse_input(load_strs("inputs/day05.txt"))
    print(f"Part 1: {message(run_9000(stacks, moves))}")
    stacks, moves = parse_input(load_strs("inputs/day05.txt"))
    print(f"Part 2: {message(run_9001(stacks, moves))}")


# --Tests--
fixture = [
    "    [D]    ",
    "[N] [C]    ",
    "[Z] [M] [P]",
    " 1   2   3 ",
    "",
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2",
]


def test_parse():
    stacks, moves = parse_input(fixture)
    assert len(stacks) == 3
    assert stacks[1] == ["Z", "N"]
    assert stacks[2] == ["M", "C", "D"]
    assert stacks[3] == ["P"]
    assert len(moves) == 4
    assert moves[0].quantity == 1
    assert moves[0].source == 2
    assert moves[0].target == 1


def test_part_1():
    stacks, moves = parse_input(fixture)
    assert message(run_9000(stacks, moves)) == "CMZ"


def test_part_2():
    stacks, moves = parse_input(fixture)
    assert message(run_9001(stacks, moves)) == "MCD"
