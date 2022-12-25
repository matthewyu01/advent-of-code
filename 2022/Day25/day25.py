with open('input.txt','r') as f:
    LINES = [line[:-1] for line in f.readlines()]
with open('test.txt','r') as f:
    test = [line[:-1] for line in f.readlines()]
    
def part1(lines=LINES): 
    s = 0
    for num in lines:
        for i,c in enumerate(num):
            power = len(num) - 1 - i
            if c.isdigit():
                s += int(c) * 5 ** power
            elif c == '-':
                s -= 1 * 5 ** power
            elif c == '=':
                s -= 2 * 5 ** power
    
    power = 0
    res = ''
    # convert to base 5 str
    while s > 0:
        mod = s % 5
        s //= 5
        power += 1
        res = str(mod) + res

    # convert to snafu
    SNAFU = ''
    carry = False
    for i in range(len(res)-1,-1,-1):
        c = int(res[i])
        if carry:
            c += 1
        if c <= 2:
            SNAFU = str(c) + SNAFU
            carry = False
        else:
            if c == 3:
                SNAFU = '=' + SNAFU
            elif c == 4:
                SNAFU = '-' + SNAFU
            else:
                SNAFU = '0' + SNAFU
            carry = True
    if carry:
        SNAFU = '1' + SNAFU
    return SNAFU
              
          
print(f'Part 1 Test Output: {part1(test)}' )
print(f'Part 1 ACTUAL: {part1(LINES)}' )
