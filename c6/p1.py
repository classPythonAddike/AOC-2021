with open(0) as f:
    inp = f.read().strip().split(",")

fishes = list(map(int, inp))

num_days = 80

for _ in range(num_days):
    num_zeroes = fishes.count(0)

    fishes = [fish - 1 if fish != 0 else 6 for fish in fishes] + num_zeroes * [8]

print(len(fishes))
