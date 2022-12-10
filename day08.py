from loader import load_strs


class Forest:
    def __init__(self, lines):
        self.rows = []
        for line in lines:
            row = [Tree(int(t)) for t in line]
            self.rows.append(row)

        self.set_visibility()
        self.scenic_score()

    def set_visibility(self):
        # Eastward
        for row in self.rows:
            tallest = -1
            for tree in row:
                if tree.height > tallest:
                    tree.visible = True
                    tallest = tree.height

        # Westward
        for row in self.rows:
            tallest = -1
            for tree in row[::-1]:
                if tree.height > tallest:
                    tree.visible = True
                    tallest = tree.height

        # Southward
        for i in range(len(self.rows[0])):
            tallest = -1
            for j in range(len(self.rows)):
                tree = self.rows[j][i]
                if tree.height > tallest:
                    tree.visible = True
                    tallest = tree.height

        # Northward
        for i in range(len(self.rows[0])):
            tallest = -1
            for j in range(len(self.rows) - 1, -1, -1):
                tree = self.rows[j][i]
                if tree.height > tallest:
                    tree.visible = True
                    tallest = tree.height

    def scenic_score(self):
        for j, row in enumerate(self.rows):
            for i, tree in enumerate(row):
                # Eastward
                view = 0
                for r in range(i + 1, len(row)):
                    view += 1
                    if self.rows[j][r].height >= tree.height:
                        break
                tree.scenic *= view

                # Westward
                view = 0
                for r in range(i - 1, -1, -1):
                    view += 1
                    if self.rows[j][r].height >= tree.height:
                        break
                tree.scenic *= view

                # Southward
                view = 0
                for r in range(j + 1, len(self.rows[0])):
                    view += 1
                    if self.rows[r][i].height >= tree.height:
                        break
                tree.scenic *= view

                # Northward
                view = 0
                for r in range(j - 1, -1, -1):
                    view += 1
                    if self.rows[r][i].height >= tree.height:
                        break
                tree.scenic *= view

    def count_visible(self):
        return sum(tree.visible for row in self.rows for tree in row)

    def max_scenic(self):
        return max(tree.scenic for row in self.rows for tree in row)


class Tree:
    def __init__(self, height):
        self.height = height
        self.visible = False
        self.scenic = 1


if __name__ == "__main__":
    forest = Forest(load_strs("inputs/day08.txt"))
    print(f"Part 1: {forest.count_visible()}")
    print(f"Part 2: {forest.max_scenic()}")


# -- Tests --

fixture = [
    "30373",
    "25512",
    "65332",
    "33549",
    "35390",
]


def test_part_1():
    assert Forest(fixture).count_visible() == 21


def test_part_2():
    assert Forest(fixture).max_scenic() == 8
