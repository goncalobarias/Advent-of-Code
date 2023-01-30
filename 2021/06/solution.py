with open("input.txt", "r") as file:
    data = list(eval(file.readline()))


def fish_counter(days):
    fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in data:
        fishes[fish] += 1
    carry = 0
    for _ in range(days):
        carry = fishes[0]
        for fish in range(1, len(fishes)):
            fishes[fish - 1] = fishes[fish]
        fishes[6] += carry
        fishes[8] = carry

    return sum(fishes)


# PART 1
print("Answer to part 1 is", fish_counter(80))

# PART 2
print("Answer to part 2 is", fish_counter(256))
