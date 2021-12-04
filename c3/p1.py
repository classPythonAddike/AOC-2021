with open(0) as f:
    inp = f.read().strip().split("\n")

columns = {
    i: "".join([o[i] for o in inp]) for i in range(len(inp[0]))
}

gamma_rate = ""
epsilon_rate = ""

for col, _bits in columns.items():
    ones = _bits.count("1")
    zeroes = _bits.count("0")

    if ones > zeroes:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        epsilon_rate += "1"
        gamma_rate += "0"

print(int(epsilon_rate, 2) * int(gamma_rate, 2))
