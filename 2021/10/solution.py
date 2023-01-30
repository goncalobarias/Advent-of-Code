data = [line.strip() for line in open("input.txt", "r")]
opening, closing = ["[", "<", "(", "{"], ["]", ">", ")", "}"]
syntax_check = {")": 3, "]": 57, "}": 1197, ">": 25137}
auto_complete = {")": 1, "]": 2, "}": 3, ">": 4}


def syntax_checker():
    points_p1, points_p2 = 0, []
    for line in range(len(data)):
        char, score, error = 0, 0, False
        while char < len(data[line]) - 1:
            syntax, next_syntax = data[line][char], data[line][char + 1]
            if syntax not in opening or next_syntax not in closing:
                char += 1
            elif opening.index(syntax) == closing.index(next_syntax):
                data[line] = data[line][:char] + data[line][char + 2 :]
                char -= 1
            else:
                error = True
                points_p1 += syntax_check[next_syntax]
                break
        if error:
            continue
        for char in reversed(data[line]):
            score = score * 5 + auto_complete[closing[opening.index(char)]]
        points_p2.append(score)

    points_p2.sort()
    return [points_p1, points_p2[len(points_p2) // 2]]


# PART 1
print("Answer to part 1 is", syntax_checker()[0])

# PART 2
print("Answer to part 2 is", syntax_checker()[1])
