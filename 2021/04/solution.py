data = [line.strip() for line in open("input.txt", "r")]
rules = list(map(int, data[0].split(",")))
boards = [
    [
        list(map(int, x.replace("  ", ",").replace(" ", ",").split(",")))
        for x in data[i - 4 : i + 1]
    ]
    for i in range(6, len(data), 6)
]


def verify_bingo(board):
    for line in board:
        if line.count(None) == 5:
            return True
    for col in range(5):
        for line in range(5):
            if board[line][col] is not None:
                break
        if line == 4 and board[line][col] is None:
            return True
    return False


def part1():
    for rule in rules:
        for i in range(len(boards)):
            boards[i] = [
                [None if x == rule else x for x in line] for line in boards[i]
            ]
            if verify_bingo(boards[i]):
                board = [
                    element
                    for line in boards[i]
                    for element in line
                    if element is not None
                ]
                return sum(board) * rule


def part2():
    for rule in rules:
        for i in reversed(range(len(boards))):
            boards[i] = [
                [None if x == rule else x for x in line] for line in boards[i]
            ]
            if verify_bingo(boards[i]):
                if len(boards) == 1:
                    board = [
                        element
                        for line in boards[i]
                        for element in line
                        if element is not None
                    ]
                    return sum(board) * rule
                del boards[i]


# PART 1
print("Answer to part 1 is", part1())

# PART 2
print("Answer to part 2 is", part2())
