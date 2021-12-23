def treat_data(txt):
    with open(txt) as file: data = file.readlines()
    rules = eval(data[0])
    del data[0:2]

    return [data, rules]


def create_boards(data):
    boards, i = [], len(data) - 1
    while i > 3:
        board = [x.replace('  ', ',') for x in data[i-4:i+1]]
        board = [x.replace(' ', ',') for x in board]
        for line in range(len(board)):
            if board[line][0] == ',': board[line] = board[line][1:]
        board = list(map(eval, board))
        boards += [board]
        i -= 6
    
    return boards


def verify_bingo(board):
    count = 0
    for line in board:
        for number in board:
            if number == '@': count += 1
        if count == len(line): return true

        


def soma(board):
    board_sum = 0
    for line in board:
        for number in line:
            if isinstance(number, int): board_sum += number

    return board_sum


def check_boards(boards, rules):
    for rule in rules:
        for board in boards:
            for line in board:
                line = ['@' for x in line if x == rule else x]
            if verify_bingo(board): return [soma(board), rule]

info = treat_data("input.txt")
print(check_boards(create_boards(info[0]), info[1]))
