with open(0) as f:
    inp = f.read().strip()

commands = map(str.split, inp.split("\n"))
commands = [[i, int(j)] for i, j in commands]

h_pos = 0
v_pos = 0

for dir, mag in commands:
    if dir == "forward":
        h_pos += mag
    elif dir == "down":
        v_pos += mag
    elif dir == "up":
        v_pos -= mag

print(h_pos * v_pos)
