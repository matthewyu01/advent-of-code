import re
import time


def num_spoken(line, number_place = 2020):
    a = time.time()
    num_memory = {}
    count_over_one = {}
    nums = [int(num) for num in re.findall(r"[0-9]+", line)]
    turn = 1

    for num in nums: #assumes input is all diff numbers
        num_memory[num] = turn
        count_over_one[num] = False
        last_num = num
        turn += 1 
    
    while turn <= number_place:
        #print(last_num)
        if count_over_one[last_num] == False: #first time
            last_num = 0
        else:
            last_times = num_memory[last_num]
            last_num = last_times[0] - last_times[1] #diff in turns between last two appearances

        over_one = count_over_one.get(last_num)
        if over_one != None: #if num has appeared
            if over_one == False: #if appeared more than once
                num_memory[last_num] = (turn,num_memory[last_num])
                count_over_one[last_num] = True
            else:
                previous_turn = num_memory[last_num][0]
                num_memory[last_num] = (turn,previous_turn)
        else:
            num_memory[last_num] = turn
            count_over_one[last_num] = False        

        turn += 1 

    return last_num


def test_func():
    assert(num_spoken('1,3,2') == 1)
    assert(num_spoken('2,1,3') == 10)
    assert(num_spoken('1,2,3') == 27)
    assert(num_spoken('2,3,1') == 78)
    assert(num_spoken('3,2,1') == 438)
    assert(num_spoken('3,1,2') == 1836)

    assert(num_spoken('3,2,1', 30000000) == 18)


if __name__ == "__main__":
    input_str = '19,0,5,1,10,13'

    #test_func()
    print(f"P1: {num_spoken(input_str)}")
    print(f"P2: {num_spoken(input_str, 30000000)}")