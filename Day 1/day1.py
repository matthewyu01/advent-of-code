nums = []
with open('input.txt', 'r') as f:
    nums = [int(line) for line in f.readlines()]

for num in nums:
    if 2020-num in nums:
        print(num)
        print(2020 - num)
        print(num * (2020-num))
        break

nums.sort()
for num in nums:
    for num2 in nums:
        if 2020-num-num2 in nums:
            print(num)
            print(2020 - num-num2)
            print(num2)
			break
            


