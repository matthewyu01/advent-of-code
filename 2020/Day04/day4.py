import re


def check_passports(batch_file):
    valid_passports_1 = 0
    valid_passports_2 = 0
    current_passport = ""
    for line in batch_file:
        if line != '\n':
            for char in line:
                if char != '\n':
                    current_passport += char
                else:
                    current_passport += " "
        else:
            if check_for_fields(current_passport):
                valid_passports_1 += 1
            if verify_fields(current_passport):
                valid_passports_2 += 1 
            current_passport = ""
    #check last passport
    if check_for_fields(current_passport):
        valid_passports_1 += 1   
    if verify_fields(current_passport):
        valid_passports_2 += 1 
    return valid_passports_1,valid_passports_2


def check_for_fields(passport):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid",]
    # if all needed fields are present
    if all(needed_field in passport for needed_field in fields):
        return True
    return False


def verify_fields(passport):
    #?=.* matches if pattern is anywhere
    birth_pattern = "byr:(19[2-9][0-9]|200[0-2]) " # byr:1920-2002
    issue_pattern = "iyr:(201[0-9]|2020) " # iyr:2010-2020
    expiration_pattern = "eyr:(202[0-9]|2030) " # eyr:2020-2030

    height_pattern = "hgt:((59|6[0-9]|7[0-6])in|1([5-8][0-9]|9[0-3])cm) " # hgt: 59-76in or 150-193cm
    hair_clr_pattern = "hcl:#[0-9a-f]{6} " # hcl:# 6 of 0-9 or a-f

    eye_clr_pattern = "ecl:(amb|blu|brn|gry|grn|hzl|oth) " #ecl:amb blu brn gry grn hzl oth
    id_pattern = "pid:[0-9]{9} "

    all_patterns = [birth_pattern, issue_pattern, expiration_pattern, height_pattern, hair_clr_pattern, eye_clr_pattern, id_pattern]

    for pattern in all_patterns:
        if not re.search(pattern,passport + " "):
            return False
    return True


def test_examples():
    #test given examples to find wrong regex pattern
    assert(not verify_fields("eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926"))
    assert(not verify_fields("iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946"))
    assert(not verify_fields("hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277"))
    assert(not verify_fields("hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007"))
    assert(verify_fields("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f "))
    assert(verify_fields("eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm "))
    assert(verify_fields("hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022 "))
    assert(verify_fields("iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719 "))


if __name__ == "__main__":
    passports = []
    with open('input.txt','r') as f:
        passports = f.readlines()
    test_examples()
    p1,p2 = check_passports(passports)
    print("Part 1: {} valid passports".format(p1))
    print("Part 2: {} valid passports".format(p2))