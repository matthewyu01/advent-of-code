def check_trees(tree_map,dx = 3,dy = 1):
    trees_encountered = 0
    x = 0
    y = 0

    map_width = len(tree_map[0])
    map_height = len(tree_map)

    while y < map_height:
        #check trees
        if tree_map[y][x] == '#':
            trees_encountered += 1

        x += dx
        y += dy
        
        if x >= map_width:
            x -= map_width
    return trees_encountered


if __name__ == "__main__":
    tree_map = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            # no new line chars
            tree_map.append([char for char in line if char != '\n'])

    print("Part 1:\n{} trees".format(check_trees(tree_map)))
    
    a = check_trees(tree_map,1,1)
    b = check_trees(tree_map,3,1)
    c = check_trees(tree_map,5,1)
    d = check_trees(tree_map,7,1)
    e = check_trees(tree_map,1,2)
    print("Part 2:\nAnswer: {}".format(a*b*c*d*e))