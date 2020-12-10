def get_fuel_required(mass):
    #ake its mass, divide by three, round down, and subtract 2
    fuel_needed = mass // 3 - 2
    if fuel_needed > 0:
        return fuel_needed
    return 0


def all_fuel_required(numbers):
    total_fuel = 0
    for mass in numbers:
        total_fuel += get_fuel_required(mass)
    return total_fuel


def all_fuel_required_2(numbers):
    total_fuel = 0
    for module_fuel in numbers:
        new_fuel = get_fuel_required(module_fuel)
        while new_fuel > 0:
            total_fuel += new_fuel
            new_fuel = get_fuel_required(new_fuel) #get more fuel for new fuel

    return total_fuel


if __name__ == "__main__":
    nums = []
    with open('input.txt','r') as f:
        for line in f.readlines():
            nums.append(int(line[:-1]))
    print(all_fuel_required(nums))
    print(all_fuel_required_2(nums))