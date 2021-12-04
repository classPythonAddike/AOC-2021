with open(0) as f:
    inp = f.read().strip().split("\n")

columns = {
    i: "".join([o[i] for o in inp]) for i in range(len(inp[0]))
}

oxygen = 0

def bit_criteria(gas: str, _bits: str) -> str:
    ones = _bits.count("1")
    zeroes = _bits.count("0")

    if gas == "o": # Oxygen
        return str(int(ones >= zeroes))
    else: # CO2
        return str(0 if ones == zeroes else int(ones < zeroes))


oxygen_valid = inp
co2_valid = inp

for col in columns:
    _bits = "".join([o[col] for o in oxygen_valid])
    valid_bit = bit_criteria("o", _bits)
    oxygen_valid = [item for item in oxygen_valid if item[col] == valid_bit]

    if len(oxygen_valid) == 1:
        break

for col in columns:
    _bits = "".join([c[col] for c in co2_valid])
    valid_bit = bit_criteria("c", _bits)
    co2_valid = [item for item in co2_valid if item[col] == valid_bit]

    if len(co2_valid) == 1:
        break

print(int(oxygen_valid[0], 2) * int(co2_valid[0], 2))
