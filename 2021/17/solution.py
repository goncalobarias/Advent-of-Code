with open("input.txt", "r") as file:
    data = file.readline().replace("..", ",").replace("=", ",").split(",")
x_min, x_max = int(data[1]), int(data[2])
y_min, y_max = int(data[4]), int(data[5])


def part1():
    return (abs(y_min) ** 2 - abs(y_min)) // 2


def position(coord, k):
    return coord * (k + 1) - k * (k + 1) // 2


def part2():
    valid_vel = set()
    for y in range(-abs(y_min), abs(y_min)):
        k = 0
        while True:
            if position(y, k) < y_min:
                break
            elif y_min <= position(y, k) <= y_max:
                for x in range(x_max + 1):
                    if (x >= k and x_min <= position(x, k) <= x_max) or (
                        x < k and x_min <= position(x, x) <= x_max
                    ):
                        valid_vel.add((x, y))
            k += 1
    return len(valid_vel)


# PART 1
print("Answer to part 1 is", part1())

# PART 2
print("Answer to part 2 is", part2())
