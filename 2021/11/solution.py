import copy

data = [[int(chr) for chr in lin.strip()] for lin in open("input.txt", "r")]


def visit_adjacent(octopus, j, i, exploded):
    for row in range(-1, 2):
        for col in range(-1, 2):
            n_row, n_col = row + i, col + j
            if not (
                0 <= n_row < len(octopus)
                and 0 <= n_col < len(octopus[0])
                and (n_col, n_row) not in exploded
            ):
                continue
            octopus[n_row][n_col] += 1
            if octopus[n_row][n_col] == 10:
                exploded += [(n_col, n_row)]
                visit_adjacent(octopus, n_col, n_row, exploded)


def octopus_simulator(part):
    octopus = copy.deepcopy(data)
    flashes, days, exploded = 0, 0, []
    while (part == 1 and days < 100) or (part == 2 and len(exploded) < 100):
        exploded = []
        for row in range(len(octopus)):
            for col in range(len(octopus[0])):
                octopus[row][col] += 1
                if octopus[row][col] == 10:
                    exploded += [(col, row)]
                    visit_adjacent(octopus, col, row, exploded)
        for (col, row) in exploded:
            octopus[row][col] = 0
        flashes += len(exploded)
        days += 1
    return flashes if part == 1 else days


# PART 1
print("Answer to part 1 is", octopus_simulator(1))

# PART 2
print("Answer to part 2 is", octopus_simulator(2))
