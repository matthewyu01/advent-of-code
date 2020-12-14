import re
import time

import multiprocessing
#import joblib


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
    first_time = int(id_list[0])
    last_index = len(id_list) - 1

    actual_ids_list = [int(num) for num in re.findall(r'[0-9]+', line)]
    max_time = max(actual_ids_list)
    max_time_str = str(max_time)
    max_time_index = id_list.index(max_time_str)

    earliest_time = max_time - max_time_index

    if len(id_list) > 1:
        second_max_time = sorted(actual_ids_list)[-2]
        second_max_index = id_list.index(str(second_max_time))
        #print(max_time_index,second_max_index)
        n = 0
        while True:
            if n % max_time == (max_time - max_time_index) and ((second_max_time - (n % second_max_time)) % second_max_time == second_max_index):
                earliest_time = n
                break
            n += 1

    
    while True:
        time = earliest_time
   
        for i,bus_id in enumerate(id_list):
            if bus_id == 'x':
                time += 1
                continue
            if time % int(bus_id) != 0:
                break
            time += 1

            if i == last_index:
                return earliest_time
        #print(earliest_time, max_time_index,max_time)    
        if len(id_list) > 1:        
            earliest_time += (max_time * second_max_time)
        else:
            earliest_time += max_time


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
    
    t0 = time.time()
    print(part2('17,x,13,19'))
    t1 = time.time()
    print(t1-t0)

    num_cores = multiprocessing.cpu_count()
    

    t0 = time.time()
    print(part2('1789,37,47,1889')) 
    t1 = time.time()
    print(t1-t0) #0.6154799461364746 without parallelization
    #explore_multiples()
    print(part2(lines[1]))