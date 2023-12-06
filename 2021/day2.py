# Advent of Code Day 2
directions = [i for i in open('day2-data.txt').read().split('\n')]
command_list = [tuple(d.split()) for d in directions]

# Part 1
def calculate_coordinates(command_list):
    '''
    Calculate horizontal position and depth of submarine

    Input: 
        command list (list): list of tuples (direction, value) where direction
            is a string with value 'forward', 'down' or 'up' and value is
            a string of an integer.
        
    Output:
        A tuple of the horizontal position and depth, represented as integers.
    '''    
    x = 0
    y = 0
    for direction, value in command_list:
        value = int(value)
        if direction == 'forward':
            x += value
        elif direction == 'down':
            y += value
        else: 
            y -= value
    return (x, y)


# Part 2
def calculate_coordinates_alt(command_list):
    '''
    Calculate horizontal position and depth of submarine

    Input: 
        command list (list): list of tuples (direction, value) where direction
            is a string with value 'forward', 'down' or 'up' and value is
            a string of an integer.
        
    Output:
        A tuple of the horizontal position and depth, represented as integers.
    '''
    x = 0
    y = 0
    aim = 0
    for direction, value in command_list:
        value = int(value)
        if direction == 'forward':
            x += value
            y += value * aim
        elif direction == 'down':
            aim += value
        else:
            aim -= value
    return (x, y)

