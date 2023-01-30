data = [line.strip().split(" ") for line in open("input.txt", "r")]


def part1():
    horizontal, depth = 0, 0
    for i in range(len(data)):
        if "forward" == data[i][0]:
            horizontal += int(data[i][1])
        elif "up" == data[i][0]:
            depth -= int(data[i][1])
        else:
            depth += int(data[i][1])

    return horizontal * depth


def part2():
    horizontal, depth, aim = 0, 0, 0
    for i in range(len(data)):
        if "forward" == data[i][0]:
            horizontal += int(data[i][1])
            depth += aim * int(data[i][1])
        elif "up" == data[i][0]:
            aim -= int(data[i][1])
        else:
            aim += int(data[i][1])

    return horizontal * depth


# PART 1
print("Answer to part 1 is", part1())

# PART 2
print("Answer to part 2 is", part2())
