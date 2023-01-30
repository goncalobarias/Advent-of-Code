data = [int(line.strip()) for line in open("input.txt", "r")]


def part1():
    increased = 0
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            increased += 1

    return increased


def part2():
    increased = 0
    for i in range(len(data) - 3):
        if data[i + 3] > data[i]:
            increased += 1

    return increased


# PART 1
print("Answer to part 1 is", part1())

# PART 2
print("Answer to part 2 is", part2())
