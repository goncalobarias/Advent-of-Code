def treat_data(txt):
    with open(txt) as file:
        data = file.readlines()

    data = list(map(lambda x: x[: len(x) - 1].split(" | "), data))
    for item in range(len(data)):
        for i in range(2):
            data[item][i] = data[item][i].split(" ")

    return data


def find_numbers(data):
    numbers = 0
    for output in data:
        for j in range(len(output[1])):
            if len(output[1][j]) in [2, 4, 3, 7]:
                numbers += 1

    return numbers


def decipher(numbers, data):
    for dec in range(len(data)):
        for num in numbers:
            if sorted(list(data[dec])) == sorted(list(num)):
                data[dec] = str(numbers.index(num))
                break

    return int("".join(data))


def find_numbers_part_2(data):
    sumation = 0
    for output in data:
        numbers = ["", "", "", "", "", "", "", "", "", ""]
        current_line = output[0]

        # Going thru the list one time to find the digits 1, 7, 4 and 8.
        for dig in current_line:
            # Find digit 1
            if len(dig) == 2:
                numbers[1] += dig

            # Find digit 7
            elif len(dig) == 3:
                numbers[7] += dig

            # Find digit 4
            elif len(dig) == 4:
                numbers[4] += dig

            # Find digit 8
            elif len(dig) == 7:
                numbers[8] += dig

        # Viewing the list a second and last time to find the other digits.
        for dig in current_line:
            # Find digit 3
            if len(dig) == 5 and numbers[1][0] in dig and numbers[1][1] in dig:
                numbers[3] += dig

            # Find digit 6
            elif len(dig) == 6 and (
                (numbers[1][0] in dig and numbers[1][1] not in dig)
                or (numbers[1][1] in dig and numbers[1][0] not in dig)
            ):
                numbers[6] += dig

            # Find digit 0
            elif (
                len(dig) == 6
                and len(list(l1 for l1 in dig if l1 not in numbers[4])) == 3
            ):
                numbers[0] += dig

            # Find digit 2
            elif (
                len(dig) == 5
                and len(list(l1 for l1 in dig if l1 not in numbers[4])) == 3
            ):
                numbers[2] += dig

            # Find digit 9
            elif (
                len(dig) == 6
                and len(list(l1 for l1 in dig if l1 not in numbers[4])) == 2
            ):
                numbers[9] += dig

            # Find digit 5
            elif (
                len(dig) == 5
                and len(list(l1 for l1 in dig if l1 not in numbers[4])) == 2
            ):
                numbers[5] += dig

        sumation += decipher(numbers, output[1])

    return sumation
