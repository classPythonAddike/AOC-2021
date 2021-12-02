
with open(0) as f:
    inp = f.read().strip()

nums = list(map(int, inp.split("\n")))
windows = [sum(nums[i:i+3]) for i in range(0, len(nums) - 2)]

count = windows[0] > windows[1]
for i in range(1, len(windows), 1):
    if windows[i] > windows[i - 1]:
        count += 1

print(count)
