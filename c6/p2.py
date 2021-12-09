with open(0) as f:
    inp = f.read().strip().split(",")

fishes = {}

for fish in list(map(int, inp)):
    fishes[fish] = fishes.get(fish, 0) + 1

for i in range(9):
    fishes[i] = fishes.get(i, 0)

num_days = 256

for _ in range(num_days):
    num_zeroes = fishes[0]

    fishes_copy = {i: 0 for i in range(9)}

    for fish in fishes:
        if fish == 0:
            fishes_copy[8] = fishes[0]
            fishes_copy[6] += fishes[0]
        else:
            fishes_copy[fish - 1] += fishes[fish]

    fishes = fishes_copy.copy()

print(sum(fishes.values()))
