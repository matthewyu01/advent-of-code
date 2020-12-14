import math


def part1(codes):
    x = 0
    y = 0 #y is in math convention, up is positive
    direction = 0 # in degrees - 0 is east
    for code in codes:
        char = code[0]
        num = int(code[1:])
        if char == 'F':
            y += math.sin(math.radians(direction)) * num
            x += math.cos(math.radians(direction)) * num
        elif char == 'N':
            y += num
        elif char == 'S':
            y -= num
        elif char == 'E':
            x += num
        elif char == 'W':
            x -= num   
        elif char == 'L':
            direction += num   
        elif char == 'R':
            direction -= num        

    return abs(x) + abs(y) #l1/manhattan dist


def part2(codes):
    ship_x = 0
    ship_y = 0
    w_delta_x = 10
    w_delta_y = 1

    for code in codes:
        wpoint_x = ship_x + w_delta_x
        wpoint_y = ship_y + w_delta_y
        char = code[0]
        num = int(code[1:])
        if char == 'F':
            for _ in range(num):
                ship_y += w_delta_y
                ship_x += w_delta_x

        elif char == 'N':
            w_delta_y += num
        elif char == 'S':
            w_delta_y -= num
        elif char == 'E':
            w_delta_x += num
        elif char == 'W':
            w_delta_x -= num   
        elif char == 'L':
            direction = math.atan2(w_delta_y,w_delta_x) # atan2 returns in rads (angle is 360/goes all round)
            length = (w_delta_y ** 2 + w_delta_x ** 2)**0.5
            direction += math.radians(num)
            w_delta_y = math.sin(direction) * length
            w_delta_x = math.cos(direction) * length

        elif char == 'R':
            direction = math.atan2(w_delta_y,w_delta_x) # atan2 returns in rads (angle is 360/goes all round)
            length = (w_delta_y ** 2 + w_delta_x ** 2)**0.5
            direction -= math.radians(num)
            w_delta_y = math.sin(direction) * length
            w_delta_x = math.cos(direction) * length  
        # print(w_delta_x, w_delta_y)
        # print(ship_x,ship_y)

    return abs(ship_x) + abs(ship_y) #l1/manhattan dist


if __name__ == "__main__":
    with open('input.txt','r') as f:
        lines = [line.strip() for line in f.readlines()]
    test_codes = [
        'F10',
        'N3',
        'F7',
        'R90',
        'F11',]
    assert(part1(test_codes)==25)
    print(f"P1: {part1(lines)}")
    assert(part2(test_codes)==286)
    print(f"P2: {part2(lines)}")            