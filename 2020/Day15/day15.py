import re


def num_spoken(line, number_place = 2020):
    num_memory = {}
    num_count = {}
    nums = [int(num) for num in re.findall(r"[0-9]+", line)]
    turn = 1

    for num in nums:
        num_memory[num] = turn
        num_count[num] = 1
        last_num = num
        turn += 1 
    
    while turn <= number_place: #returns 2020th num
        #print(last_num)
        if num_count[last_num] == 1: #first time
            last_num = 0
            count = num_count.get(last_num)
            if count != None: #if it's been in
                num_count[last_num] = count + 1
                if count == 1:
                    num_memory[last_num] = (turn,num_memory[last_num])
                else:
                    previous_turn = num_memory[last_num][0]
                    num_memory[last_num] = (turn,previous_turn)
            else:
                num_memory[last_num] = turn
                num_count[last_num] = 1
        else:
            last_num = num_memory[last_num][0] - num_memory[last_num][1]
            count = num_count.get(last_num)
            if count != None: #if it's been in
                num_count[last_num] = count + 1
                if count == 1:
                    num_memory[last_num] = (turn,num_memory[last_num])
                else:
                    previous_turn = num_memory[last_num][0]
                    num_memory[last_num] = (turn,previous_turn)
            else:
                num_memory[last_num] = turn
                num_count[last_num] = 1

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