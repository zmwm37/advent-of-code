import numpy as np

def read_input(file_path):
    with open(file_path) as f:
        coords = f.readlines()
    return coords

# parsing from Andres' solution: https://github.com/acrucetta/advent_of_code/tree/master/2021
# make parsing shorter?
def parse_input(coordinates):
    directions = {}
    max_x = 0
    max_y = 0
    for i,coord in enumerate(coordinates):
        coords = coord.split('\n')[0].split('->')
        coords_lst = tuple(map(lambda x: x.strip().split(','), coords))
        coords_int = tuple(map(lambda x: tuple(map(lambda y: int(y.strip()), x)), coords_lst))
        x1, x2 = coords_int[0][0], coords_int[1][0]
        y1, y2 = coords_int[0][1], coords_int[1][1]
        if x2 > max_x or x1 > max_x:
            max_x = max(x2, x1)
        if y2 > max_y or y1 > max_y:
            max_y = max(y2, y1)
        directions[i] = coords_int
    return directions, max_x, max_y

# test_file_path = 'day5-test-data.txt'
# raw_test_input = read_input(test_file_path)
file_path = 'day5-data.txt'
raw_input = read_input(file_path)
  
    
def count_vents(input, diagonal = False):
    '''
    Create a matrix where each value is the number of vents at the (i,j) 
    position

    Input:
        input: list of unparsed strings of vent coordinates in 
            (x1,y1) -> (x2, y2) format
        diagonal: boolean indicating whether diagonal vents should be included
            (True) or excluded (False)
    '''
    directions, max_x, max_y = parse_input(input)

    # create a matrix of 0s that is NxM
    vents = np.zeros((max_x + 1, max_y + 1))  

    for (x1,y1), (x2,y2) in directions.values():
        row_start = min(y1, y2) 
        row_end = max(y1, y2) + 1
        col_start = min(x1, x2)
        col_end = max(x1, x2) + 1
        # case 1 - vertical or horizontal line
        if x1 == x2 or y1 == y2:
            vents[row_start: row_end, col_start: col_end] += 1
        elif diagonal:
            # case 2 - top left to bottom right diagonal
            if (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2):
                for i in range(abs(x2 - x1) + 1):
                    vents[row_start + i, col_start + i] += 1
            # case 3 - bottom left to top right diagonal
            else:
                for i in range(abs(x2 - x1) + 1):
                    vents[row_end - (i + 1), col_start + i] += 1


    return vents

part_1_vents = count_vents(raw_input)
# count where two+ vents overlap
(part_1_vents >= 2).sum()

part_2_vents = count_vents(raw_input, diagonal = True)
(part_2_vents >= 2).sum()
