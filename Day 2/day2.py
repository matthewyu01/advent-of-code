lines = []
with open('input.txt', 'r') as f:
    lines = [line for line in f.readlines()]

valid_count_1 = 0
valid_count_2 = 0
for line in lines: #example input-   1-9 x: xwjgxtmrzxzmkx
    line_list = line.split(' ')

    #get numbers
    numbers_txt = line_list[0]
    nums = numbers_txt.split('-')
    
    num1 = int(nums[0])
    num2 = int(nums[1])

    #get letter
    letter = line_list[1][0] 

    #get password
    password = line_list[2]

    letter_count = password.count(letter)
    #checks for valid password
    if letter_count >= num1 and letter_count <= num2:
        valid_count_1 += 1
    
    #convert indices to 0 index
    num1 -= 1
    num2 -= 1
    # only one index must be letter
    if (password[num1] == letter) !=  (password[num2] == letter): #logical xor
        valid_count_2 += 1

print(valid_count_1)
print(valid_count_2)