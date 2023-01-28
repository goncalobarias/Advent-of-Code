opening, closing = ["[", "<", "(", "{"], ["]", ">", ")", "}"]


def treat_data(txt):
    with open(txt) as file:
        data = file.readlines()
    data = list(map(lambda line: list(line[: len(line) - 1]), data))

    return data


def get_index(char):
    if char in opening:
        return opening.index(char)
    else:
        return closing.index(char)


def syntax_error_check(data):
    errors, LINES = [], len(data)

    for line in range(LINES):
        char = 0
        while char + 1 <= len(data[line]) - 1:
            syntax, next_syntax = data[line][char], data[line][char + 1]
            if syntax in opening and next_syntax in closing:
                if get_index(syntax) != get_index(next_syntax):
                    errors += [next_syntax]
                    data[line] = data[line][:char] + data[line][char + 2 :]
                    break
                else:
                    data[line] = data[line][:char] + data[line][char + 2 :]
                    char -= 1
            else:
                char += 1

    return errors


def point_checker(errors):
    points = 0
    for error in errors:
        if error == ")":
            points += 3
        elif error == "]":
            points += 57
        elif error == "}":
            points += 1197
        else:
            points += 25137

    return points


def complete_lines(line):
    pattern = ""
    for char in range(len(line) - 1, -1, -1):
        pattern += closing[get_index(line[char])]

    return pattern


def get_points(patterns):
    points = []
    for pattern in patterns:
        point = 0
        for closer in pattern:
            point *= 5
            if closer == ")":
                point += 1
            elif closer == "]":
                point += 2
            elif closer == "}":
                point += 3
            else:
                point += 4
        points += [point]

    return points


def check_incompletenessk(data):
    patterns, points, LINES = [], [], len(data)

    for line in range(LINES):
        char, error = 0, ""
        while char + 1 <= len(data[line]) - 1:
            syntax, next_syntax = data[line][char], data[line][char + 1]
            if syntax in opening and next_syntax in closing:
                if get_index(syntax) != get_index(next_syntax):
                    error = next_syntax
                    data[line] = data[line][:char] + data[line][char + 2 :]
                    break
                else:
                    data[line] = data[line][:char] + data[line][char + 2 :]
                    char -= 1
            else:
                char += 1
        if error == "":
            patterns += [complete_lines(data[line])]

    points = get_points(patterns)
    points.sort()

    return points[len(points) // 2]
