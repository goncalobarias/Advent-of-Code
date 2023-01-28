def treat_data(txt):
    with open(txt) as file:
        data = file.readlines()
    rules = eval(data[0])
    del data[0:2]

    return [data, rules]


def create_boards(data):
    boards, i = [], len(data) - 1
    while i > 3:
        board = [x.replace("  ", ",") for x in data[i - 4 : i + 1]]
        board = [x.replace(" ", ",") for x in board]
        for line in range(len(board)):
            if board[line][0] == ",":
                board[line] = board[line][1:]
        board = list(map(eval, board))
        boards += [board]
        i -= 6

    return boards


def verify_bingo(board):
    size = len(board[0])
    for line in board:
        count = 0
        for number in line:
            if number == "@":
                count += 1
        if count == size:
            return True

    for col in range(size):
        cont = 0
        for i in range(size):
            if board[i][col] == "@":
                cont += 1
        if cont == size:
            return True

    return False


def soma(board):
    board_sum = 0
    for line in board:
        for number in line:
            if isinstance(number, int):
                board_sum += number

    return board_sum


def check_boards(boards, rules):
    for rule in rules:
        for board in boards:
            for line in range(len(board)):
                board[line] = ["@" if x == rule else x for x in board[line]]
            if verify_bingo(board):
                return [soma(board), rule]


def check_boards_part2(boards, rules):
    for rule in rules:
        for board in range(len(boards)):
            if boards[board] != "i'm done":
                for line in range(len(boards[board])):
                    boards[board][line] = [
                        "@" if x == rule else x for x in boards[board][line]
                    ]
                if verify_bingo(boards[board]):
                    print([soma(boards[board]), rule])
                    boards[board] = "i'm done"
