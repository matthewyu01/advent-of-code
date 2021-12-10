""" https://adventofcode.com/2021/day/3 """


def get_lines():
    with open('input.txt', 'r') as f:
        # ignore \n at end of each line
        return [line[:-1] for line in f.readlines()]


lines = get_lines()

# Part 1
gamma_rate = ''
epsilon_rate = ''

l = len(lines[0])  # length of line frmo input
for i in range(l):
    zeros = 0
    ones = 0
    for line in lines:
        if line[i] == '0':
            zeros += 1
        else:
            ones += 1

    if zeros > ones:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'
power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
print(f"Power Consumption: {power_consumption}")

# Part 2

test_lines = ['00100',
              '11110',
              '10110',
              '10111',
              '10101',
              '01111',
              '00111',
              '11100',
              '10000',
              '11001',
              '00010',
              '01010', ]

life_support_rating = 0
oxygen_generator_rating = 0
co2_scrubber_rating = 0

o_lines = lines.copy()
c_lines = lines.copy()

for i in range(l):
    o_zeros = []
    o_ones = []
    c_zeros = []
    c_ones = []
    for line in o_lines:
        if line[i] == '0':
            o_zeros.append(line)
        else:
            o_ones.append(line)
    for line in c_lines:
        if line[i] == '0':
            c_zeros.append(line)
        else:
            c_ones.append(line)

    if len(o_zeros) > len(o_ones):
        o_lines = o_zeros.copy()
    else:  # tiebreaker goes to ones
        o_lines = o_ones.copy()

    if len(c_zeros) <= len(c_ones):  # tiebreaker goes to zeros
        c_lines = c_zeros.copy()
    else:
        c_lines = c_ones.copy()

    if len(o_lines) == 1 and oxygen_generator_rating == 0:
        oxygen_generator_rating = int(o_lines[0], 2)
    if len(c_lines) == 1 and co2_scrubber_rating == 0:
        co2_scrubber_rating = int(c_lines[0], 2)

print(oxygen_generator_rating)
print(co2_scrubber_rating)
life_support_rating = oxygen_generator_rating * co2_scrubber_rating
print(f"Life Support Rating: {life_support_rating}")
