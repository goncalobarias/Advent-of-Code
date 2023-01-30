with open("input.txt", "r") as file:
    data = sorted(list(map(int, eval(file.readline()))))


def apply(value):
    return int(((1 + abs(value)) / 2) * abs(value))


def get_fuel_usage(fn):
    fuel_min = float("inf")
    for i in range(data[0], data[-1] + 1):
        fuel_usage = 0
        for e in data:
            fuel_usage += fn(e - i)
        fuel_min = min(fuel_min, fuel_usage)
    return fuel_min


# PART 1
print("Answer to part 1 is", get_fuel_usage(abs))

# PART 2
print("Answer to part 2 is", get_fuel_usage(apply))
