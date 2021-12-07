from collections import Counter
from typing import List, Tuple

def slope(line: List[Tuple]) -> float:
    x1 = line[0][0]
    y1 = line[0][1]
    x2 = line[1][0]
    y2 = line[1][1]
    return (y2 - y1) / (x2 - x1) if x2 != x1 else float("inf")

with open(0) as f:
    inp = f.read().strip().split("\n")

coordinates = [
    [tuple(map(int, coord.split(","))) for coord in line.split(" -> ")] for line in inp
]

horizontal_lines = [line_seg for line_seg in coordinates if line_seg[0][1] == line_seg[1][1]]
vertical_lines = [line_seg for line_seg in coordinates if line_seg[0][0] == line_seg[1][0]]
sloped_lines = [line_seg for line_seg in coordinates if slope(line_seg) in [1, -1]]

vertices = Counter()

for line_seg in horizontal_lines:
    start = min([line_seg[0][0], line_seg[1][0]])
    end = max([line_seg[0][0], line_seg[1][0]])

    vertices.update([(x_coord, line_seg[0][1]) for x_coord in range(start, end + 1)])

for line_seg in vertical_lines:
    start = min([line_seg[0][1], line_seg[1][1]])
    end = max([line_seg[0][1], line_seg[1][1]])

    vertices.update([(line_seg[0][0], y_coord) for y_coord in range(start, end + 1)])

for line_seg in sloped_lines:
    if slope(line_seg) == 1:
        min_x, min_y = min([line_seg[0][0], line_seg[1][0]]), min([line_seg[0][1], line_seg[1][1]])
        max_x = max([line_seg[0][0], line_seg[1][0]])

        vertices.update([(min_x + i, min_y + i) for i in range(max_x + 1 - min_x)])

for line_seg in sloped_lines:
    if slope(line_seg) == -1:
        min_x, max_y = min([line_seg[0][0], line_seg[1][0]]), max([line_seg[0][1], line_seg[1][1]])
        max_x = max([line_seg[0][0], line_seg[1][0]])

        vertices.update([(min_x + i, max_y - i) for i in range(max_x + 1 - min_x)])

print(len([i for i in vertices if vertices[i] > 1]))
