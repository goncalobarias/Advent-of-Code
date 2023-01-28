def treat_data(txt):
    with open(txt) as file:
        data = sorted(list(eval(file.readline())))

    return data


def check_fuel(data):
    fuel_usages = []
    for i in range(len(data)):
        fuel = map(lambda x: abs(x - i), data)
        fuel_usages.append(sum(fuel))
    fuel_usages.sort()

    return fuel_usages[0]


def arithmetic_sum(value):
    return int(((1 + value) / 2) * value)


def check_fuel_part_2(data):
    fuel_usages = []
    for i in range(len(data)):
        fuel = map(lambda x: arithmetic_sum(abs(x - i)), data)
        fuel_usages.append(sum(fuel))
    fuel_usages.sort()

    return fuel_usages[0]
