
# create two dictionaries:
        # keys are row index with numbers, values are tuples of start and end columns of #'s
        # keys are row index with symbols, values are column index
# for each entry in number dict, check if symbol in boundary 
        # i - 1: i + 1
        # min(j) - 1: max(j) + 1
special_characters = "!\"#$%&'()*+,-/:;<=>?@[\]^_`{|}~"
def is_symbol(c:str)->bool:
    if c in special_characters:
        return True
    else:
        return False

def is_int(c:str)->bool:
    '''
    Test if character is integer
    '''
    try:
        int(c)
    except:
        return False
    return True

def find_val_cols(string:str)->tuple:
    num_idx = []
    sym_idx = []
    gear_idx = []
    p = None
    q = None
    prev_number = False
    current_number = False
    number = ''
    for i, c in enumerate(string):
        # if integer and prev not, add p
        if is_int(c):
            current_number = True
                number += c
            if not prev_number: # current char number, prev not
                p = i
                prev_number = True
            if i + 1 == len(string): # current char number, end of string
                q = i
                num_idx.append((p, q))
                prev_number = False
                p, q = None, None
            # current char number, prev is, not end of string
        else:
            current_number = False 
            if prev_number: # current char not, prev is
                q = i - 1
                num_idx.append((p, q))
                prev_number = False
                p, q = None, None
            # current chart not, prev not
            if is_symbol(c):
                sym_idx.append(i)
    return (num_idx, sym_idx)

def build_dicts(lines:list)->tuple:
    num_dict = {}
    sym_dict = {-1:[],len(lines): []}
    for i, line in enumerate(lines):
        num_idx, sym_idx = find_val_cols(line)
        num_dict[i] = num_idx; sym_dict[i] = sym_idx
    
    return (num_dict, sym_dict)

def number_by_symbol(i, p, q, sym_dict)->bool:
    if (p - 1 in sym_dict[i]) or (q + 1 in sym_dict[i]):
        return True
    else:
        #print(f'sym_dict[i-1] {sym_dict[i-1]}')
        #print(f'sym_dict[i+1] {sym_dict[i+1]}')
        for j in range((p-1),(q+2)):
            #print(f'j: {j}')
            
            # TODOP: fix indexing so not out of bounds for rows
            if (j in sym_dict[i-1]) or (j in sym_dict[i+1]):
                return True
    return False
    
def get_part_numbers(num_dict:dict, sym_dict:dict, numbers:list):
    part_numbers = []
    for i, val in num_dict.items():
        #print(f'ROW: {i}---')
        for tup in val:
            #print(f'tup: {tup}')
            p, q = tup
            #print(f'by symbol?: {number_by_symbol(i, p, q, sym_dict)}')
            if number_by_symbol(i, p, q, sym_dict):
                part_numbers.append(int(numbers[i][p:q+1]))

    return part_numbers 

if __name__ == "__main__":
    FILEPATH = 'day3.txt'
    with open(FILEPATH) as f:
        raw = f.readlines()
        lines = [i.strip('\n') for i in raw]
        num_dict, sym_dict = build_dicts(lines)
        part_numbers = get_part_numbers(num_dict, sym_dict, lines)
        #print(f'Part numbers: {part_numbers}')
        print(f'Sum of part numbers: {sum(part_numbers)}')
        