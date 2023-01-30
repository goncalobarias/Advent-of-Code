data = [line.strip() for line in open("input.txt", "r")]


def part1():
    gamma = 0
    for position in range(len(data[0])):
        zeros = 0
        for i in range(len(data)):
            if data[i][position] == "0":
                zeros += 1
        if 2 * zeros < len(data):
            gamma += 2 ** (len(data[0]) - 1 - position)
    epsilon = ~gamma & (2 ** len(data[0]) - 1)

    return gamma * epsilon


def part2(mode):
    d = data
    for position in range(len(d[0])):
        if len(d) > 1:
            zeros = 0
            for i in range(len(d)):
                if d[i][position] == "0":
                    zeros += 1

            if (2 * zeros > len(d) and mode == 0) or (
                2 * zeros <= len(d) and mode == 1
            ):
                d = list(filter(lambda x: (x[position] == "0"), d))
            elif (2 * zeros <= len(d) and mode == 0) or (
                2 * zeros > len(d) and mode == 1
            ):
                d = list(filter(lambda x: x[position] == "1", d))

    return int(d[0], 2)


# PART 1
print("Answer to part 1 is", part1())

# PART 2
print("Answer to part 2 is", part2(0) * part2(1))
