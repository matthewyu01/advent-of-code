def get_bags_rules(lines):
    bags_rules = {}
    for line in lines:
        outer_bag_index = line.find("bag")
        outer_bag = line[:outer_bag_index-1]

        if line.find("no")!=-1:
            bags_rules[outer_bag] = None

        else:
            last_index = len(line) - 1
            inner_bags = []
            for i,char in enumerate(line):
                if char.isdigit():
                    bag_start_index = i + 2
                    bag_end_index = line.find("bag",bag_start_index,last_index) - 1
                    bag = line[bag_start_index:bag_end_index]
                    inner_bags.append(bag)

            bags_rules[outer_bag] = inner_bags

    return bags_rules    


def contains_bag(lines,inner_bag):
    bags_rules = get_bags_rules(lines)
    valid_outer_bags = []
    possible_bags = bags_rules.keys()
    for possible_bag in possible_bags: #go through every outer bag
        if inside_bag(bags_rules,possible_bag,inner_bag):
            valid_outer_bags.append(possible_bag)

    return valid_outer_bags


def inside_bag(bags_rules,outer_bag,inner_bag):
    value = bags_rules[outer_bag]
    if value == None:
        return False
    if inner_bag in value:
        return True
    else: 
        for possible_bag in value:
            if inside_bag(bags_rules,possible_bag,inner_bag): #if contains
                return True
        return False #if it's recursively gone through everything, return false


def get_bags_rules_with_counts(lines):
    bags_rules = {}
    for line in lines:
        outer_bag_index = line.find("bag")
        outer_bag = line[:outer_bag_index-1]

        if line.find("no")!=-1:
            bags_rules[outer_bag] = None

        else:
            last_index = len(line) - 1
            inner_bags = []
            for i,char in enumerate(line):
                if char.isdigit():
                    count = int(char)
                    bag_start_index = i + 2
                    bag_end_index = line.find("bag",bag_start_index,last_index) - 1
                    bag = line[bag_start_index:bag_end_index]
                    inner_bags.append((bag,count))

            bags_rules[outer_bag] = inner_bags

    return bags_rules  


def count_inner_bags(bags_rules,outer_bag):
    inner_bag_count = 0
    inner_bags = bags_rules[outer_bag]
    if inner_bags == None:
        return inner_bag_count
    #print(bags_rules[outer_bag][1][1])# for count
    for bag, count in inner_bags:

        inner_bag_count += (count + count * count_inner_bags(bags_rules,bag)) #count bag itself and multiply by inner amount

    return inner_bag_count


if __name__ == "__main__":
    with open('input.txt','r') as f:
        lines = f.readlines()
    #part 1
    contains_shiny_gold = contains_bag(lines,"shiny gold")
    print(contains_shiny_gold)
    print(len(contains_shiny_gold))
    #part 2
    print(count_inner_bags(get_bags_rules_with_counts(lines),"shiny gold"))