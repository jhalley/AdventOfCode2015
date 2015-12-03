# Perfectly spherical houses in a vacuum

def num_houses_visited():
    filename = raw_input('Enter filename: ')
    with open(filename) as f:
        directions = f.readlines()[0].strip()

    houses = {'1,1': True}
    curr_x = 1
    curr_y = 1

    for direction in directions:
        if direction == '^':
            curr_y += 1
        elif direction == '>':
            curr_x += 1
        elif direction == 'v':
            curr_y -= 1
        elif direction == '<':
            curr_x -= 1

        houses[','.join([str(curr_x), str(curr_y)])] = True

    print len(houses.keys())


def num_houses_visited_with_robosanta():
    filename = raw_input('Enter filename: ')
    with open(filename) as f:
        directions = f.readlines()[0].strip()

    houses = {'1,1': True}
    curr_x = 1
    curr_y = 1

    # Process santa first
    for direction in directions[::2]:
        if direction == '^':
            curr_y += 1
        elif direction == '>':
            curr_x += 1
        elif direction == 'v':
            curr_y -= 1
        elif direction == '<':
            curr_x -= 1

        houses[','.join([str(curr_x), str(curr_y)])] = True

    # Process robosanta
    curr_x = 1
    curr_y = 1
    for direction in directions[1::2]:
        if direction == '^':
            curr_y += 1
        elif direction == '>':
            curr_x += 1
        elif direction == 'v':
            curr_y -= 1
        elif direction == '<':
            curr_x -= 1

        houses[','.join([str(curr_x), str(curr_y)])] = True

    print len(houses.keys())


# num_houses_visited()
num_houses_visited_with_robosanta()