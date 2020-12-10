def check_passwords_1(min_num,max_num):
    valid = 0
    for n in range(min_num,max_num+1):
        valid_pw = False
        str_num = str(n)
        i = 0
        while i < len(str_num) - 1:
            char = str_num[i]
            if char > str_num[i+1]:
                valid_pw = False
                break
            if char == str_num[i+1]:
                valid_pw = True
            i += 1
        if valid_pw:
            valid += 1

    return valid


def check_passwords_2(min_num,max_num):
    valid = 0
    for n in range(min_num,max_num+1):
        valid_pw = True
        double_match = False
        str_num = str(n)
        i = 0
        while i < len(str_num):
            char = str_num[i]
            if i > 0 and char < str_num[i-1]:
                valid_pw = False
                break

            if i < len(str_num) - 1 and char == str_num[i+1]:
                j = 2
                while i+j < len(str_num) and char == str_num[i+j]:# if matches more than once
                    j += 1
                if j == 2:
                    i += 1
                    double_match = True
                else:
                    i += (j-1)
                        
            i += 1

        if valid_pw and double_match:
            print(n)
            valid += 1

    return valid


print(check_passwords_1(197487,673251))
print(check_passwords_2(197487,673251))
