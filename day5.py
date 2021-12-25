import numpy as np

file_path = 'day5-data.txt'
def read_input(file_path):
    with open(file_path) as f:
        coords = f.readlines()
    return coords

# parsing from Andres' solution
def parse_input(coordinates):
    directions = {}
    max_x = 0
    max_y = 0
    for i,coord in enumerate(coordinates):
        coords = coord.split('\n')[0].split('->')
        coords_lst = list(map(lambda x: x.strip().split(','), coords))
        coords_int = list(map(lambda x: list(map(lambda y: int(y.strip()), x)), coords_lst)) # modify to tuples?
        x1, x2 = coords_int[0][0], coords_int[1][0]
        y1, y2 = coords_int[0][1], coords_int[1][1]
        if x2 > max_x or x1 > max_x:
            max_x = max(x2, x1)
        if y2 > max_y or y1 > max_y:
            max_y = max(y2, y1)
        directions[i] = coords_int
    return directions, max_x, max_y

# approach
raw_input = read_input(file_path)
directions, max_x, max_y = parse_input(raw_input)
# create a matrix of 0s that is NxM
vents = np.zeros((max_x, max_y))
for coord in 
# loop through each line and add 1 to location in diagram
# if the value is greater than one (or maybe just 2), add to set
# get length of set
