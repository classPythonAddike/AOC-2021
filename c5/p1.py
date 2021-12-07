from collections import Counter

with open(0) as f:
    inp = f.read().strip().split("\n")

coordinates = [
    [tuple(map(int, coord.split(","))) for coord in line.split(" -> ")] for line in inp
]

horizontal_lines = [line_seg for line_seg in coordinates if line_seg[0][1] == line_seg[1][1]]
vertical_lines = [line_seg for line_seg in coordinates if line_seg[0][0] == line_seg[1][0]]

vertices = Counter()

for line_seg in horizontal_lines:
    start = min([line_seg[0][0], line_seg[1][0]])
    end = max([line_seg[0][0], line_seg[1][0]])

    vertices.update([(x_coord, line_seg[0][1]) for x_coord in range(start, end + 1)])

for line_seg in vertical_lines:
    start = min([line_seg[0][1], line_seg[1][1]])
    end = max([line_seg[0][1], line_seg[1][1]])

    vertices.update([(line_seg[0][0], y_coord) for y_coord in range(start, end + 1)])

print(len([i for i in vertices if vertices[i] > 1]))
