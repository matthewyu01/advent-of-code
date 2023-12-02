
with open('input.txt','r') as f:
    LINES = [line[:-1] for line in f.readlines()]
with open('test1.txt','r') as f:
    test1 = [line[:-1] for line in f.readlines()]
try:
    with open('test2.txt','r') as f:
        test2 = [line[:-1] for line in f.readlines()]
except:
    test2 = test1


def part1(lines=LINES): 
    r = 12
    g = 13
    b = 14
    res = 0
    for l in lines:
        n = ''
        id = int(l.split(' ')[1][:-1])
        # print(id)
        right = l.split(': ')[1]
        # print(right)
        # right = right.replace(';', ',')  should've read the problem more carefully...
        nums = right.split('; ')
        
        flag = True
        for s in nums:
            r1,g1,b1 = 0,0,0
            for c in s.split(', '):
                # print(c)
                n = int(c.split(' ')[0])
                # print(n)
                if c.endswith('blue'):
                    b1 += n
                if c.endswith('red'):
                    r1 += n
                if c.endswith('green'):
                    g1 += n

            if not (b1 <= b and r1 <= r and g1<=g) and flag:
                flag = False
                break
        if flag:
            res += id
        
    return res


print(f'Part 1 Test Output: {part1(test1)}' )
print(f'Part 1 ACTUAL: {part1(LINES)}' )


def part2(lines=LINES):     
    res = 0
    for l in lines:
        n = ''
        right = l.split(': ')[1]
        nums = right.split('; ')
        
        mr = 0
        mg = 0
        mb = 0
        for s in nums:
            r1,g1,b1 = 0,0,0
            for c in s.split(', '):
                # print(c)
                n = int(c.split(' ')[0])
                # print(n)
                if c.endswith('blue'):
                    b1 += n
                if c.endswith('red'):
                    r1 += n
                if c.endswith('green'):
                    g1 += n

            mr = max(r1, mr)
            mg = max(g1, mg)
            mb = max(b1, mb)
            
        # print(mr*mg*mb)
        res += mr*mg*mb
        
    return res
          
print(f'Part 2 Test Output: {part2(test2)}' )
print(f'Part 2 ACTUAL: {part2(LINES)}' )
