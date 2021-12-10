with open(0) as f:
    inp = f.read().strip().split("\n")

outputs = [i.split("|")[-1].strip().split() for i in inp]
counts = [len([a for a in i if len(a) in [2, 4, 3, 7]]) for i in outputs]

print(sum(counts))
