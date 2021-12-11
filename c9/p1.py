with open(0) as f:
    inp = [[*map(int, i)] for i in f.read().strip().split("\n")]

inp = [[100] * (len(inp[0]) + 2)] + [[100] + i + [100] for i in inp] + [[100] * (len(inp[0]) + 2)]

low_points = []

for i in range(1, len(inp) - 1):
    for j in range(1, len(inp[0]) - 1):
        if inp[i][j] < min([inp[i - 1][j], inp[i + 1][j], inp[i][j - 1], inp[i][j + 1]]):
            low_points += [inp[i][j]]

print(sum(low_points) + len(low_points))
