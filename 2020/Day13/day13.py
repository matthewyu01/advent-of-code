import re
import time


def part1(lines):
    earliest_time = int(lines[0])
    num_list = [int(num) for num in re.findall(r'[0-9]+', lines[1])]
    
    if len(num_list) > 0:
        first_num = num_list[0]
        earliest_bus_id = first_num
        min_wait_time = first_num - (earliest_time % first_num)
        #mistake - min_wait_time = earliest_time % first_num
    if len(num_list) > 1:
        for num in num_list[1:]:
            wait_time = num - (earliest_time % num)
            if wait_time < min_wait_time:
                earliest_bus_id = num
                min_wait_time = wait_time
        #print(earliest_bus_id, min_wait_time)
        return earliest_bus_id * min_wait_time

    return "Incorrect Input"


def part2(line):
    id_list = line.split(',')
    actual_ids_list = [int(num) for num in re.findall(r'[0-9]+', line)]

    first_num = actual_ids_list[0]

    nums_aligned = []
    aligned_product = 1
    aligned_time = 0
    max_aligned = len(actual_ids_list) - 1
    
    times_left_sorted = sorted(actual_ids_list[1:])

    while len(nums_aligned) < max_aligned:
        n = aligned_time
        max_time = times_left_sorted[-1]
        max_time_index = id_list.index(str(max_time))
        times_left_sorted.remove(max_time)
        while True:
            #needed the last %max_time since max_time_index > max_time
            if (n % max_time == ((max_time - max_time_index) % max_time)): 
                nums_aligned.append(n)
                aligned_product *= max_time
                aligned_time = n
                break
            n += aligned_product

    while True:
        if aligned_time % first_num == 0:
            return aligned_time
        aligned_time += aligned_product

    return aligned_time
	

def explore_multiples():
    m1 = 911
    m1_index = 41
    m2 = 827
    m2_index = 72 

    for n in range(1000000):
        if n % m1 == (m1 - m1_index) and n % m2 == (m2-m2_index):
            print(n)

    # diff btwn n is m1*m2 - this is used for ln 59


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    print(part1(['939', '7,13,x,x,59,x,31,19']))
    print(f"P1: {part1(lines)}\n\n")
    
    # t0 = time.time()
    # print(part2('17,x,13,19'))
    # t1 = time.time()
    # print(t1-t0)
    #assert(part2('67,7,x,59,61') == 1261476)
    # t0 = time.time()
    # print(part2('1789,37,47,1889')) 
    # t1 = time.time()
    # print(t1-t0) 
    #explore_multiples()
    t0 = time.time()
    print(f"P2: {part2(lines[1])}") 
    t1 = time.time()
    print(t1-t0)#basically same run time as less complicated inputs