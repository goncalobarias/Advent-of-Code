data, max_x, max_y = [], 0, 0
for i in open("input.txt", "r"):
    data += [list(map(int, i.strip().replace(" -> ", ",").split(",")))]
    max_x = max(max_x, data[-1][0], data[-1][2])
    max_y = max(max_y, data[-1][1], data[-1][3])


def day5(part):
    matrix = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    count = 0
    for line in data:
        if line[2] != line[0]:
            y_start = min(line[1], line[3])
            slope = (line[3] - line[1]) / (line[2] - line[0])
            if slope != 0 and part == 1:
                continue
            if slope == -1:
                y_start = max(line[1], line[3])
            for x in range(min(line[0], line[2]), max(line[0], line[2]) + 1):
                y = int((x - min(line[0], line[2])) * slope + y_start)
                matrix[y][x] += 1
                if matrix[y][x] == 2:
                    count += 1
        else:
            for y in range(min(line[1], line[3]), max(line[1], line[3]) + 1):
                matrix[y][line[0]] += 1
                if matrix[y][line[0]] == 2:
                    count += 1
    return count


# PART 1
print("Answer to part 1 is", day5(1))

# PART 2
print("Answer to part 2 is", day5(2))
