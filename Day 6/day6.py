with open('input.txt', 'r') as f:
    lines = f.readlines()

total_count_1 = 0
total_count_2 = 0

letter_list = []
possible_letter_list = []
 
for index, line in enumerate(lines):
    if line == '\n':
        total_count_2 += len(possible_letter_list) #add count for shared yes
        #reset lists for new group
        letter_list = []
        possible_letter_list = []
        continue
    
    for letter in line:
        if letter.isalpha():
            #part 1
            if letter not in letter_list:
                total_count_1 += 1
                letter_list.append(letter)
                
            #part 2
            if index == 0 and letter not in possible_letter_list:
                    possible_letter_list.append(letter)
                
            elif index > 0:
                if lines[index-1] == '\n': #if first person of group
                    if letter not in possible_letter_list:
                        possible_letter_list.append(letter)

    new_list = []
    if index > 0:
        if lines[index-1] != '\n': # if not first person, compare letters
            for possible_letter in possible_letter_list:
                if possible_letter in line:
                   new_list.append(possible_letter)
            possible_letter_list = new_list

    if index + 1 == len(lines): # last line 
        total_count_2 += len(possible_letter_list) 
        
print(total_count_1) # part 1 - 6748
print(total_count_2) # part 2 - 3445







