
with open('input.txt','r') as f:
    LINES = [line[:-1] for line in f.readlines()]
with open('test1.txt','r') as f:
    test1 = [line[:-1] for line in f.readlines()]
with open('test2.txt','r') as f:
    test2 = [line[:-1] for line in f.readlines()]


def part1(lines=LINES): 
    res = 0
    for l in lines:
        n = ''
        first = False
        last = ''
        for c in l:
            if c.isnumeric():
                if not first:
                    n = c
                    first = True

                last = c
        n += last
        res += int(n)
    
    return res

print(f'Part 1 Test Output: {part1(test1)}' )
print(f'Part 1 ACTUAL: {part1(LINES)}' )


def part2(lines=LINES): 
    nums = {'one': 1, 'two': 2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    res = 0
    for l in lines:
        n = ''
        first = False
        last = ''
        for i, c in enumerate(l):
            try:
                if c.isnumeric():
                    if not first:
                        n = c
                        first = True
                    last = c
                    
                elif l[i:i+3] in nums:
                    if not first:
                        first = True
                        n = str(nums[l[i:i+3]])
                    last =  nums[l[i:i+3]]
                elif l[i:i+4] in nums:
                    if not first:
                        first = True
                        n = str(nums[l[i:i+4]])
                    last =  nums[l[i:i+4]]
                elif l[i:i+5] in nums:
                    if not first:
                        first = True
                        n = str(nums[l[i:i+5]])
                    last = nums[l[i:i+5]]
            except:
                pass
        n += str(last)
        # print(n)
        res += int(n)
    
    return res
          
print(f'Part 2 Test Output: {part2(test2)}' )
print(f'Part 2 ACTUAL: {part2(LINES)}' )
