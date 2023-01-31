from collections import Counter

data = [line.strip().split(" -> ") for line in open("input.txt", "r")]
polymer = data[0][0]
template, letters = {}, Counter()
for t in data[2:]:
    template[t[0]] = t[0][0] + t[1] + t[0][1]
    letters[t[1]] = 0
for e in polymer:
    letters[e] += 1


def polymerization(polymer, steps):
    polymers = letters.copy()
    duplicates = Counter()
    for i in range(len(polymer) - 1):
        duplicates[polymer[i : i + 2]] += 1
    for _ in range(steps):
        new_duplicates = Counter()
        for e in duplicates.keys():
            polymers[template[e][1]] += duplicates[e]
            new_duplicates[template[e][0:2]] += duplicates[e]
            new_duplicates[template[e][1:3]] += duplicates[e]
        duplicates = new_duplicates
    return max(polymers.values()) - min(polymers.values())


# PART 1
print("Answer to part 1 is", polymerization(polymer, 10))

# PART 2
print("Answer to part 2 is", polymerization(polymer, 40))
