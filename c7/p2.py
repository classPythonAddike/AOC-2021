inp = list(map(int, input().split(",")))


# [(point, distance) . . . .]
distances = []

for point in range(min(inp), max(inp)):
    total_distance = 0
    for locus in inp:
        displacement = abs(point - locus)
        total_distance += displacement * (displacement + 1) // 2

    distances.append((point, total_distance))

print(sorted(distances, key=lambda a: a[1])[0])
