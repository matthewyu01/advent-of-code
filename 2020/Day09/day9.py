"""
https://adventofcode.com/2020/day/9
"""


def find_first_non_sum(numbers,check_previous): # part 1
    for i in range(check_previous,len(numbers)):
        number_found = False
        for j in range(i-check_previous,i):
            if number_found:
                break
            for k in range(i-check_previous,i):
                if j == k:
                    continue
                if numbers[j] + numbers[k] == numbers[i]:
                    number_found = True
                    break
        if not number_found:
            return numbers[i]
                
    return 0


def find_contiguous_sum(numbers,cont_sum): #part 2
    length = len(numbers)
    for i in range(length):
        first = numbers[i]
        contiguous_list = [first]
        accumulator = first
        for j in range(i+1,length):
            addend = numbers[j]
            contiguous_list.append(addend)
            accumulator += addend
            if accumulator == cont_sum and len(contiguous_list) >= 2:
                contiguous_list.sort()
                smallest = contiguous_list[0]
                largest = contiguous_list[-1]
                return smallest + largest
            elif accumulator > cont_sum:
                break
            
    return -1                


if __name__ == "__main__":
    nums = []
    with open('input.txt','r') as f:
        for line in f.readlines():
            nums.append(int(line[:-1]))
    part_1_answer = find_first_non_sum(nums,25)
    print(part_1_answer)
    print(find_contiguous_sum(nums,part_1_answer))