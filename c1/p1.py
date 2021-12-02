with open(0) as f:
    inp = f.read().strip()

nums = list(map(int, inp.split("\n")))

count = nums[0] > nums[1]

for i in range(1, len(nums), 1):
    if nums[i] > nums[i - 1]:
        count += 1

print(count)
