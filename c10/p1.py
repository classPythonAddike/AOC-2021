with open(0) as f:
    inp = f.read().strip().split("\n")

_sum = 0

print()

for line in inp:
    bracket_map = {"{": "}", "(": ")", "[": "]", "<": ">" }
    open_bracket = []
    expects = lambda: open_bracket[-1] if len(open_bracket) > 0 else ""

    print(line)
    open_brack_sum = 0
    close_brack_sum = 0
    for open_brack, close_brack in bracket_map.items():
        open_brack_sum += line.count(open_brack)
        close_brack_sum += line.count(close_brack)

#    if open_brack_sum != close_brack_sum:
#        print(open_brack_sum, close_brack_sum, "incomplete\n")
#        continue

    for char in line:
        if char in bracket_map.keys():
            open_bracket.append(char)
        elif char == expects():
            open_bracket.pop(-1)
        else:
            _sum += {
                ")": 3,
                "]": 57,
                "}": 1197,
                ">": 25137
            }[char]
            break

print(_sum)
