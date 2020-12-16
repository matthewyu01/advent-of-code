import re


def part1(lines):
    memory = {}
    bit_mask = ''
    for line in lines:
        if line[:4] == 'mask':
            bit_mask = line[7:]
        else:
            nums = [int(num) for num in re.findall(r'[0-9]+', line)]
            addr = nums[0]
            binary_str = bin(nums[1])[2:] #converts number to binary. 2: since str starts with 0b
            binary_str = binary_str.rjust(36,'0') #fill in 0s to the left

            new_str = ''
            for i,char in enumerate(bit_mask):
                if char == 'X':
                    new_str += binary_str[i]
                else:
                    new_str += char
            memory[addr] = int(new_str, 2)

    values_sum = 0
    for key in memory:
        values_sum += memory[key]
    return values_sum


def part2(lines):
    memory = {}
    bit_mask = ''
    for line in lines:
        if line[:4] == 'mask':
            bit_mask = line[7:]
        else:
            addrs = []
            nums = [int(num) for num in re.findall(r'[0-9]+', line)]
            addr = nums[0]
            value = nums[1]
            addr = bin(addr)[2:]
            addr_str = str(addr)
            addr_str = addr_str.rjust(36,'0') 
            
            new_addr_mask = ''
            for i,char in enumerate(bit_mask):
                if char == 'X':
                    #save floating bit
                    new_addr_mask += 'X'  
                elif char == '0':
                    new_addr_mask += addr_str[i]
                elif char == '1':
                    new_addr_mask += '1'
            addrs = get_addrs(new_addr_mask)
            for address in addrs:
                memory[int(address,2)] = value

    values_sum = 0
    for key in memory:
        values_sum += memory[key]
    return values_sum


def get_addrs(result_mask, previous_str = ""):
    addrs = [""]
    for i, char in enumerate(result_mask):
        if char == 'X':
            new_addrs = []
            for i in range(len(addrs)):
                # add 0 and 1 to possible addrs
                new_addrs.append(addrs[i] + '0') 
                new_addrs.append(addrs[i] + '1')
            addrs = new_addrs.copy()
        else:
            new_addrs = []
            for i in range(len(addrs)):
                #add new char to every addr
                new_addrs.append(addrs[i] + char)
                
            addrs = new_addrs.copy()

    return addrs


if __name__ == '__main__':
    with open('input.txt','r') as f:
        lines = [line.strip() for line in f.readlines()]
    test_lines = [
        'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
        'mem[8] = 11',
        'mem[7] = 101',
        'mem[8] = 0]',]
    assert(part1(test_lines) == 165)
    print(f"P1: {part1(lines)}")
    test_lines = [
        'mask = 000000000000000000000000000000X1001X',
        'mem[42] = 100',
        'mask = 00000000000000000000000000000000X0XX',
        'mem[26] = 1',
    ]
    assert(part2(test_lines) == 208)
    print(f"P2: {part2(lines)}")