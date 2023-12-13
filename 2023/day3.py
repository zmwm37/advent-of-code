
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

def add_to_gear_index(i:int, j:int, num:int, gear_index:dict):
    '''
    Add gear to appropriate place in gear_index dictionary.
    '''
    if gear_index.get(i):
        if gear_index[i].get(j):
            gear_index[i][j].append(num)
        else:
            gear_index[i][j] = [num]
    else:
        gear_index[i] = {j: [num]}
        

def scan_for_symbol(indexes:tuple, strings:tuple, gear_index:dict)->int:
    '''
    Once a number has been completed, scan neighborhood for symbols. If it is, return
    the number, otherwise return -1.
    '''
    p, q, i = indexes
    prev, current, future = strings
    num = int(current[p:q + 1])
    return_num = False
    if p - 1 >= 0:
        if current[p - 1] in special_characters:
            if current[p - 1] == '*':
                add_to_gear_index(i, p - 1, num, gear_index)
            return_num = True
    if q + 1 < len(current):
        if current[q + 1] in special_characters:
            if current[q + 1] == '*':
                add_to_gear_index(i, q + 1, num, gear_index)
            return_num = True
   
    new_p = max(0, p - 1)
    new_q = min(len(current), q + 2)
    for j in range(new_p, new_q):
        if prev != '':
            if prev[j] in special_characters:
                return_num = True
                if prev[j] == '*':
                    add_to_gear_index(i-1, j, num, gear_index)
        if future != '':
            if future[j] in special_characters:
                return_num = True
                if future[j] == '*':
                    add_to_gear_index(i+1, j, num, gear_index)

    if return_num:
        return num
    else:
        return -1

    
def is_int(c:str)->bool:
    '''
    Test if character is integer
    '''
    try:
        int(c)
    except:
        return False
    return True

def find_val_cols(string:str, prev_string:str, next_string:str, number_list:list, gear_index:dict, row_idx:int)->tuple:
    '''
    In a line, find numbes and scan for symbols
    '''
    p = None
    q = None
    prev_number = False
    current_number = False
    for i, c in enumerate(string):
        # if integer and prev not, add p
        if is_int(c):
            current_number = True
            if not prev_number: # current char number, prev not -> start new number
                p = i
                prev_number = True
            if i + 1 == len(string): # current char number, end of string -> scan symbol
                q = i
                number_with_symbol = scan_for_symbol(indexes=(p, q, row_idx), strings=(prev_string, string, next_string), gear_index=gear_index)
                if number_with_symbol != -1:
                    number_list.append(number_with_symbol)
                prev_number = False
                p, q = None, None
            # current char number, prev is, not end of string
        else:
            current_number = False 
            if prev_number: # current char not, prev is -> end of number 
                q = i - 1
                number_with_symbol = scan_for_symbol(indexes=(p, q, row_idx), strings=(prev_string, string, next_string), gear_index=gear_index)
                if number_with_symbol != -1:
                    number_list.append(number_with_symbol)
                prev_number = False
                p, q = None, None
            # current chart not, prev not

def get_gear_ratio_sum(gear_index:dict)->int:
    gear_ratios = []
    for k, v in gear_index.items():
        for j, u in v.items():
            if len(u) == 2:
                product = 1
                for val in u:
                    product = product * val
                gear_ratios.append(product)
    return sum(gear_ratios)
    

def get_numbers(lines:list)->tuple:
    number_list = []
    gear_index = {}
    for idx, line in enumerate(lines):
        if idx == 0:
            prev = ''
        else:
            prev = lines[idx - 1]
        if idx == len(lines) - 1:
            future = ''
        else:
            future = lines[idx + 1]
    
        find_val_cols(line, prev, future, number_list, gear_index, idx)
        
    number_sum = sum(number_list)print
    gear_ratio_sum = get_gear_ratio_sum(gear_index)
    return (number_sum, gear_ratio_sum)


if __name__ == "__main__":
    FILEPATH = 'day3.txt'
    with open(FILEPATH) as f:
        raw = f.readlines()
        lines = [i.strip('\n') for i in raw]
        number_sum, gear_ratio_sum = get_numbers(lines)
        print(f'Sum of part numbers: {number_sum}')
        print(f'Sum of gear ratios: {gear_ratio_sum}')
        