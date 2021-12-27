opening, closing = ['[', '<', '(', '{'], [']', '>', ')', '}']
def treat_data(txt):
    with open(txt) as file: data = file.readlines()
    data = list(map(lambda x: list(x[:len(x) - 1]), data))

    return data


### PART 1 ###
def syntax_error_check(data):
    char, errors = 0, []

    for line in range(len(data)):
        char = 0
        while char + 1 < len(data[line]) - 1:
            if (data[line][char] in opening 
                and data[line][char + 1] in closing):
                if (opening.index(data[line][char]) 
                    != closing.index(data[line][char + 1])):
                    errors += [data[line][char + 1]]
                    data[line] = data[line][:char] + data[line][char + 2:]
                    char -= 1
                    break
                else:
                    data[line] = data[line][:char] + data[line][char + 2:]
                    char -= 1
            else: char += 1

    return errors


def point_checker(errors):
    score = 0
    for error in errors:
        if error == ')': score += 3
        elif error == ']': score += 57
        elif error == '}': score += 1197
        else: score += 25137

    return score


### PART 2 ###



data = treat_data("input.txt")
print(point_checker(syntax_error_check(data)))
