from day3 import *
test_input = [
    '467..114..', 
    '...*..$../', 
    '..35..633.', 
    '.2.......8'
]

test_input_1 = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..'
]

def test_find_idx0():
    num_idx, sym_idx = find_val_cols(test_input[0])
    assert num_idx == [(0,2), (5,7)]

def test_find_idx1():
    num_idx, sym_idx = find_val_cols(test_input[1])
    assert num_idx == []

def test_find_idx2():
    num_idx, sym_idx = find_val_cols(test_input[3])
    assert num_idx == [(1,1), (9,9)]

def test_find_idx3():
    num_idx, sym_idx = find_val_cols(test_input[1])
    assert sym_idx == [3, 6, 9]

def test_number_by_symbol0():
    
