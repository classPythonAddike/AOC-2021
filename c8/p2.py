from typing import Generator, List


with open(0) as f:
    inp = f.read().strip().split("\n")


def solve_segments(lines: List[List[List[str]]]):
    numbers = {
        0: set(["t", "tl", "tr", "bl", "br", "b"]),
        1: set(["tr", "br"]),
        2: set(["t", "tr", "m", "bl", "b"]),
        3: set(["t", "tr", "m", "br", "b"]),
        4: set(["tl", "m", "tr", "br"]),
        5: set(["t", "tl", "m", "br", "b"]),
        6: set(["t", "tl", "m", "br", "b", "bl"]),
        7: set(["t", "tr", "br"]),
        8: set(["tl", "t", "tr", "m", "bl", "b", "br"]),
        9: set(["tr", "t", "tl", "m", "br", "b"])
    }

    """
    1, 4, 7, 8 - unique number of segments (1 - 2, 4 - 4, 7 - 3, 8 - 7)

    0 - 6
    2 - 5
    3 - 5
    5 - 5
    6 - 6
    9 - 6
    """

    """
    t - 8 occurences, appears in 0, 2, 3, 5, 6, 7, 8, 9
    tl - 6 occurences
    tr - 8 occurences, appears in 0, 1, 2, 3, 4, 7, 8, 9
    m - 7 occurences, appears in 2, 3, 4, 5, 6, 8, 9
    bl - 4 occurences
    br - 9 occurences
    b - 7 occurences, appears in 0, 2, 3, 5, 6, 8, 9
    """

    _sum = 0


    for inp, output in lines:
        
        variables = {}

        # inp will look like ["ceg" "gedcfb" "ec" "eabfdg" "gcdabe" "baged" "cabgf" "gbaec" "fecagdb" "eacd"]
        variables["tl"] = [i for i in "abcdefg" if sum([i in j for j in inp]) == 6][0]
        variables["bl"] = [i for i in "abcdefg" if sum([i in j for j in inp]) == 4][0]
        variables["br"] = [i for i in "abcdefg" if sum([i in j for j in inp]) == 9][0]

        one = [i for i in inp if len(i) == 2][0]
        four = [i for i in inp if len(i) == 4][0]
        seven = [i for i in inp if len(i) == 3][0]
        eight = [i for i in inp if len(i) == 7][0]

        variables["t"] = [i for i in "abcdefg" if sum([i in j for j in inp]) == 8 and i not in one and i not in four][0]
        variables["tr"] = [i for i in "abcdefg" if sum([i in j for j in inp]) == 8 and i in one and i in four][0]
        variables["m"] = [i for i in "abcdefg" if sum([i in j for j in inp]) == 7 and i in four][0]
        variables["b"] = [i for i in "abcdefg" if sum([i in j for j in inp]) == 7 and i not in four][0]

        one, four, seven, eight = set(one), set(four), set(seven), set(eight)

        numbers_map = {}
        for i in numbers:
            numbers_map[i] = set([variables[j] for j in numbers[i]])

        num = ""

        for i in output:
            for j in numbers_map:
                if numbers_map[j] == set(i):
                    num += str(j)
                    break
        _sum += int(num)
    
    return _sum

print(
    solve_segments(
        [[i.split("|")[0].strip().split(), i.split("|")[1].strip().split()] for i in inp]
    )
)

