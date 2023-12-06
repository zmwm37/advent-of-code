digit_word_dict = {
    'o': {'one'},
    't': {'two', 'three'},
    'f': {'four', 'five'},
    's': {'six', 'seven'},
    'e': {'eight'},
    'n': {'nine'}
}

reverse_digit_word_dict = {
    'e': {'eno', 'eerht', 'evif', 'enin'},
    'o': {'owt'},
    'r': {'ruof'},
    'x': {'xis'},
    'n': {'neves'},
    't': {'thgie'}
}

word_digit_map = {
    'one': '1',
    'eno': '1', 
    'two': '2',
    'owt': '2',
    'three': '3',
    'eerht': '3',
    'four': '4',
    'ruof': '4',
    'five': '5',
    'evif': '5', 
    'six': '6',
    'xis': '6',
    'seven': '7',
    'neves': '7',
    'eight': '8',
    'thgie': '8',
    'nine': '9',
    'enin': '9'
}


def is_int(c:str)->bool:
    '''
    Test if character is integer
    '''
    try:
        int(c)
    except:
        return False
    return True


def is_spelled_int(c:str, s:str, i:int, reverse=False)->str:
    '''
    Test if spelled integer present.
    '''
    if reverse:
        options = reverse_digit_word_dict.get(c)
    else:
        options = digit_word_dict.get(c)
    if options:
        for option in options:
            end = len(option) + i
            if option == s[i:end]:
                return word_digit_map[option]
    return None


def find_int(s:str, reverse=False)->str:
    '''
    Iterate through string and return first "digit"
    '''
    # TODO: check for spelled digits
    for i, c in enumerate(s):
        if is_int(c):
            return c
        elif (c in digit_word_dict.keys()) | (c in reverse_digit_word_dict.keys()):
            integer = is_spelled_int(c, s, i, reverse=reverse)
            if integer:
                return integer
    return None


def get_code(s:str, code_list:list):
    '''
    Get code from string and add to code_list
    '''
    p = find_int(s)
    reversed_s = s[::-1]
    q = find_int(reversed_s, reverse=True)
    if (p == None) | (q == None):
        TypeError('p or q is None')
    else:
        code = int(p + q)
        code_list.append(code)

# for each string:
    # for each character:
        # go from front
        # if character is int:
            # return int
        # else if start of number string
            # return string converted to int
        # else:
            # continue
    

if __name__ == "__main__":
    FILEPATH = 'day1.txt'
    with open(FILEPATH) as f:
        code_list = []
        raw = f.readlines()
        lines = [i.strip('\n') for i in raw]
        for line in lines:
            get_code(line, code_list)
        
        print(f'CODE SUM: {sum(code_list)}')
