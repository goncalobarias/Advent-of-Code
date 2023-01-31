data = [lin.replace("=", ",").split(",") for lin in open("input.txt", "r")]
for i in range(len(data)):
    if data[i][0] == "\n":
        paper = {tuple(map(int, lin)) for lin in data[:i]}
        folds = [[fold[0], int(fold[1])] for fold in data[i + 1 :]]
        break


def fold_paper(paper):
    for fold in folds:
        tmp_paper = paper.copy()
        for p in paper:
            if fold[0][-1] == "x" and p[0] > fold[1]:
                tmp_paper.add((2 * fold[1] - p[0], p[1]))
                tmp_paper.remove(p)
            elif fold[0][-1] == "y" and p[1] > fold[1]:
                tmp_paper.add((p[0], 2 * fold[1] - p[1]))
                tmp_paper.remove(p)
        paper = tmp_paper
        if fold == folds[0]:
            print("Answer to part 1 is", len(paper))

    print("Answer to part 2 is")
    x_max, y_max = max([p[0] for p in paper]), max([p[1] for p in paper])
    real_paper = [[" " for _ in range(x_max + 1)] for _ in range(y_max + 1)]
    for point in paper:
        real_paper[point[1]][point[0]] = "█"
    for lin in real_paper:
        print("".join(lin))


fold_paper(paper)
