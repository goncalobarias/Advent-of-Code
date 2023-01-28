with open("input.txt") as file:
    data = list(map(int, file.readlines()))


def increase_counter(data):
    increased = 0
    for depth in range(len(data)):
        try:
            if data[depth] > data[depth - 1]:
                increased += 1
        except Exception:
            pass

    return increased


sums = []
for depth in range(len(data)):
    try:
        sums += [data[depth] + data[depth + 1] + data[depth + 2]]
    except Exception:
        break
