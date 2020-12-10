def find_jolt_chain(nums):
    one_dif = 0
    two_dif = 0
    thr_dif = 1 #for device at end
    nums.sort()
    for i,num in enumerate(nums):
        if i == 0:
            diff = num
        else:
            diff = num - nums[i-1]

        if diff == 1:
            one_dif += 1
        elif diff == 2:
            two_dif += 1
        elif diff == 3:
            thr_dif += 1

        else:
            print(f"Last adapter: {num}")
            break

    return one_dif, two_dif, thr_dif


if __name__ == "__main__":
    nums = []
    with open('input.txt','r') as f:
        for line in f.readlines():
            nums.append(int(line[:-1]))  
    one, _, three = find_jolt_chain(nums)
    print(one*three)