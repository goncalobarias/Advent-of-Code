data = [line.strip().split(" | ") for line in open("input.txt", "r")]
data = [[x[0].split(" "), x[1].split(" ")] for x in data]
num_code = {2: 1, 3: 7, 4: 4, 7: 8}


def part1():
    sum = 0
    for [_, output] in data:
        for j in output:
            if len(j) in [2, 4, 3, 7]:
                sum += 1

    return sum


def part2():
    sum = 0
    for [input, output] in data:
        numbers = ["", "", "", "", "", "", "", "", "", ""]
        for dig in input:
            if len(dig) in [2, 3, 4, 7]:
                numbers[num_code[len(dig)]] += dig

        for dig in input:
            if len(dig) == 5 and numbers[1][0] in dig and numbers[1][1] in dig:
                numbers[3] += dig
            elif (
                len(dig) == 5
                and len(list(l1 for l1 in dig if l1 in numbers[4])) == 2
            ):
                numbers[2] += dig
            elif len(dig) == 5:
                numbers[5] += dig
            elif (
                len(dig) == 6
                and len(list(l1 for l1 in dig if l1 in numbers[4])) == 4
            ):
                numbers[9] += dig
            elif (
                len(dig) == 6 and numbers[1][0] in dig and numbers[1][1] in dig
            ):
                numbers[0] += dig
            elif len(dig) == 6:
                numbers[6] += dig

        for dec in range(len(output)):
            for num in numbers:
                if sorted(list(output[dec])) == sorted(list(num)):
                    output[dec] = str(numbers.index(num))
                    break

        sum += int("".join(output))

    return sum


# PART 1
print("Answer to part 1 is", part1())

# PART 2
print("Answer to part 2 is", part2())
