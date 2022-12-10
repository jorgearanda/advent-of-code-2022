from loader import load_strs


def parse(lines):
    wd = {}
    fs = {".": wd}
    mode = "cmd"
    for line in lines[1:]:
        tokens = line.split()
        if mode == "ls":
            if tokens[0] == "$":
                mode = "cmd"
            else:
                wd[tokens[1]] = (
                    {"..": wd, "/": fs} if tokens[0] == "dir" else int(tokens[0])
                )
                continue
        if tokens[1] == "ls":
            mode = "ls"
        if tokens[1] == "cd":
            wd = wd[tokens[2]]

    traverse(fs)
    fs["_unused"] = 70_000_000 - fs["_size"]

    return fs


def traverse(node):
    if type(node) == int:
        return node
    node["_size"] = sum(
        traverse(v) for k, v in node.items() if k not in ["..", "/", "_size", "_unused"]
    )
    return node["_size"]


def find_under(node, limit=100_000):
    found = 0
    if type(node) == dict:
        if node["_size"] <= limit:
            found += node["_size"]
        found += sum(
            find_under(v, limit)
            for k, v in node.items()
            if type(v) == dict and k not in ["..", "/"]
        )
    return found


def find_deletion_candidates(node, target, candidates):
    if type(node) == dict:
        if node["_size"] >= target:
            candidates.append(node["_size"])
        for k, v in node.items():
            if type(v) == dict and k not in ["..", "/"]:
                find_deletion_candidates(v, target, candidates)


def best_candidate(fs):
    candidates = []
    find_deletion_candidates(fs, 30_000_000 - fs["_unused"], candidates)
    return min(candidates)


if __name__ == "__main__":
    fs = parse(load_strs("inputs/day07.txt"))
    print(f"Part 1: {find_under(fs)}")
    print(f"Part 2: {best_candidate(fs)}")

# -- Tests --

fixture = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
]


def test_part_1():
    fs = parse(fixture)
    assert find_under(fs) == 95437


def test_part_2():
    fs = parse(fixture)
    assert best_candidate(fs) == 24933642
