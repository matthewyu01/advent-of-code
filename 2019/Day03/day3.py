def get_intersections(instructions, center = [0,0]):
    inters = []
    wire_1_points = {}
    wire_2_points = {}
    wire_num = 0

    for wire in instructions:
        steps = 0
        wire_num += 1
        current_x = center[0]
        current_y = center[1]
        for instruction in wire:  
            direction = instruction[0]
            number = int(instruction[1:])
            #print(number)
            for i in range(number):
                steps += 1
                if direction == 'R':
                    current_x += 1
                elif direction == 'L':
                    current_x -= 1
                elif direction == 'D':
                    current_y += 1
                elif direction == 'U':
                    current_y -= 1
                key = str(current_x) + ',' + str(current_y)
                if wire_num == 1:
                    if wire_1_points.get(key): #if intersection already found
                        if wire_1_points.get(key) < steps: #if more steps, skip
                            continue
                    wire_1_points[key] = steps
                elif wire_num == 2:
                    if wire_2_points.get(key): #if intersection already found
                        if wire_2_points.get(key) < steps: #if more steps, skip
                            continue
                    wire_2_points[key] = steps

    for point in wire_1_points.keys():
        if wire_2_points.get(point): #if intersection
            num_strings = point.split(',')
            steps_1 = wire_1_points.get(point)
            steps_2 = wire_2_points.get(point)
            total_steps = steps_1 + steps_2
            inters.append([int(num_strings[0]),int(num_strings[1]), total_steps])
    
    return inters


def find_closest_intersection(intersections, center = [0,0]):
    closest = intersections[0]
    inter = intersections[0]
    closest_dist = abs(center[0] - inter[0]) + abs(center[1] - inter[1])

    if len(intersections) > 1:
        for inter in intersections[1:]:
            l1_dist = abs(center[0] - inter[0]) + abs(center[1] - inter[1])
            if l1_dist < closest_dist:
                closest_dist = l1_dist
                closest = inter

    return closest, closest_dist


def find_fewest_steps(instructions):
    intersections = get_intersections(instructions)
    smallest_steps = intersections[0][2]
    for inter in intersections:
        steps = inter[2]
        if steps < smallest_steps:
            smallest_steps = steps


    return smallest_steps


def get_instructions():
    instructions = []
    with open('input.txt','r') as f:
        for line in f.readlines():
            instructions.append(line[:-1].split(',')) #line[:-1] to get rid of \n
    return instructions


def test_instructions():
    return [['R8','U5','L5','D3'], ['U7','R6','D4','L4']]


if __name__ == "__main__":
    wire_instructions = get_instructions()
    #wire_instructions = test_instructions()
    intersections = get_intersections(wire_instructions)
    #print(intersections)
    _, closest_distance = find_closest_intersection(intersections)
    print(closest_distance)
    print(find_fewest_steps(wire_instructions))