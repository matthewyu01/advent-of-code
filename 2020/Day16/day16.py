import re


def part1(lines):
    error_rate = 0
    #find ranges
    ranges = []
    i = 0
    for i, line in enumerate(lines):
        current_ranges = []
        if line == "":
            break
        current_ranges = [int(num_str) for num_str in re.findall(r"[0-9]+", line)]
        ranges.append((current_ranges[0], current_ranges[1])) #assumes 4 nums per line
        ranges.append((current_ranges[2], current_ranges[3]))

    get_tickets = False

    for line in lines[i:]:
        #tickets are after nearby txt
        if line[:6] == "nearby":
            get_tickets = True
        if get_tickets == True:
            current_nums = [int(num_str) for num_str in re.findall(r"[0-9]+", line)]
            for num in current_nums:
                in_range = False
                for num_range in ranges:
                    if num >= num_range[0] and num <= num_range[1]:
                        in_range = True
                        break
                if in_range == False:
                    error_rate += num
                    break

    return error_rate
    

if __name__ == "__main__":
    test_lines = [
        'class: 1-3 or 5-7',
        'row: 6-11 or 33-44',
        'seat: 13-40 or 45-50',
        '',
        'your ticket:',
        '7,1,14',
        '',
        'nearby tickets:',
        '7,3,47',
        '40,4,50',
        '55,2,20',
        '38,6,12',]
    
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    assert(part1(test_lines) == 71)
    print(f"P1: {part1(lines)}")
