from typing import List, Tuple


with open(0) as f:
    inp = [[*map(int, i)] for i in f.read().strip().split("\n")]

inp = [[9] * (len(inp[0]) + 2)] + [[9] + i + [9] for i in inp] + [[9] * (len(inp[0]) + 2)]

low_points = []

for i in range(1, len(inp) - 1):
    for j in range(1, len(inp[0]) - 1):
        if inp[i][j] < min([inp[i - 1][j], inp[i + 1][j], inp[i][j - 1], inp[i][j + 1]]):
            low_points += [(i, j)]


def nearby_basins(matrix, x, y) -> List[Tuple[int, int]]:
    basins = []
    neighbours = [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1)
    ]

    if matrix[x][y] == 9:
        return []

    for X, Y in neighbours:
        if 9 > matrix[X][Y] >= matrix[x][y]:
            basins.append((X, Y))

    return basins

def get_basin_count(pos_x, pos_y, matrix, passed_positions):

    for basin_x, basin_y in nearby_basins(matrix, pos_x, pos_y):
        if (basin_x, basin_y) not in passed_positions:

            passed_positions.append((basin_x, basin_y))
            passed_positions = get_basin_count(
                basin_x,
                basin_y,
                matrix,
                passed_positions
            )

    return passed_positions

global_seen = []
basin_sizes = []

for x, y in low_points:
    basin = get_basin_count(x, y, inp, [(x, y)])
    global_seen += basin
    basin_sizes += [len(basin)]

basin_sizes = sorted(basin_sizes)
print(basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1])
