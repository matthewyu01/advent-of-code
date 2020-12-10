from functools import cache 

nums = [0]
with open('input.txt','r') as f:
    for line in f.readlines():
        nums.append(int(line[:-1]))  

nums.sort()
nums_length = len(nums)

@cache #memoization - store in cache 
#added in Py3.9, use lru_cache for previous
def count_chains(n):
    ways = 0
    if n + 1 == nums_length: #if at end - base case
        return 1

    # check if number of ways can split
    else:
        for i, num2 in enumerate(nums[n+1:n+4], start = n+1): 
            # for every next number within 3
            if num2 - nums[n] <= 3:    
                ways += count_chains(i)

    return ways

print(count_chains(0))