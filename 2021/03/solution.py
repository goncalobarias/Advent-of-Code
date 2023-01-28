def binary_decimal(bin_num):
    def aux(bin_num, value, position):
        if bin_num == "":
            return value

        return aux(
            bin_num[: len(bin_num) - 1],
            value + int(bin_num[-1]) * 2**position,
            position + 1,
        )

    return aux(bin_num, 0, 0)


with open("input.txt") as file:
    data = list(map(lambda x: x[: len(x) - 1], file.readlines()))


def part1():
    gamma = ""
    for position in range(len(data[0])):
        zeros, ones = 0, 0
        for number in range(len(data)):
            if data[number][position] == "0":
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            gamma += "0"
        else:
            gamma += "1"
    epsilon = "".join(["1" if x == "0" else "0" for x in gamma])

    return binary_decimal(gamma) * binary_decimal(epsilon)


def part2(mode):
    data_processed = data
    for position in range(len(data_processed[0])):
        if len(data_processed) > 1:
            zeros, ones = 0, 0
            for number in range(len(data_processed)):
                if data_processed[number][position] == "0":
                    zeros += 1
                else:
                    ones += 1
            if (zeros > ones and mode == 0) or (zeros <= ones and mode == 1):
                data_processed = list(
                    filter(lambda x: x[position] == "0", data_processed)
                )
            elif (zeros <= ones and mode == 0) or (zeros > ones and mode == 1):
                data_processed = list(
                    filter(lambda x: x[position] == "1", data_processed)
                )
        else:
            break

    return binary_decimal(data_processed[0])
