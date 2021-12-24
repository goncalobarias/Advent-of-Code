def treat_data(txt):
    with open(txt) as file: data = list(eval(file.readline()))
    
    return data


def count_fish(data):
    fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in data:
        fishes[fish] += 1

    return fishes


def lanternfish_creator(fishes):
    for day in range(1, 257):
        fishes_resetting = fishes[0]
        for type in range(8):
            fishes[type] = fishes[type + 1]
        fishes[8] = fishes_resetting
        fishes[6] += fishes_resetting

    return sum(fishes)
