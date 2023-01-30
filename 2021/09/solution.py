data = [line.strip() for line in open("input.txt", "r")]


def find_surround_points(map, coord):
    points = list(
        filter(
            lambda x: 0 <= x[0] < len(map[0]) and 0 <= x[1] < len(map),
            [
                (coord[0], coord[1] - 1),
                (coord[0] + 1, coord[1]),
                (coord[0], coord[1] + 1),
                (coord[0] - 1, coord[1]),
            ],
        )
    )
    return points


def part1():
    risk_lev = 0
    for line in range(len(data)):
        for col in range(len(data[0])):
            pp = (col, line)
            points = find_surround_points(data, pp)
            bigger_points = list(
                filter(
                    lambda x: int(data[x[1]][x[0]]) > int(data[pp[1]][pp[0]]),
                    points,
                )
            )
            if len(bigger_points) == len(points):
                risk_lev += int(data[pp[1]][pp[0]]) + 1
    return risk_lev


def check_points(point, blacklist):
    size, waiting = 0, [point]
    blacklist.append(waiting[0])
    while len(waiting) != 0:
        size += 1
        points = find_surround_points(data, waiting[0])
        waiting.remove(waiting[0])
        for point in points:
            if point in blacklist or int(data[point[1]][point[0]]) == 9:
                continue
            blacklist.append(point)
            waiting.append(point)
    return size


def part2():
    sizes, blacklist = [], []
    for line in range(len(data)):
        for col in range(len(data[0])):
            if int(data[line][col]) != 9:
                continue
            points = find_surround_points(data, (col, line))
            for pp in points:
                if int(data[pp[1]][pp[0]]) != 9 and pp not in blacklist:
                    point = pp
                    sizes += [check_points(point, blacklist)]
    sizes.sort()
    return sizes[-1] * sizes[-2] * sizes[-3]


# PART 1
print("Answer to part 1 is", part1())

# PART 2
print("Answer to part 2 is", part2())
