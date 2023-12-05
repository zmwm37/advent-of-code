def is_int(x):
    try:
        int(x)
    except:
        return False
    return True

def find_int(s, reverse=False):
    if reverse:
        s = reversed(s)
    for i in s:
        if is_int(i):
            return i
    return None

def get_code(s:str, code_list:list):
    p = find_int(s)
    q = find_int(s, reverse=True)
    if (p == None) | (q == None):
        TypeError('p or q is None')
    code = int(p+q)
    code_list.append(code)
    
FILEPATH = 'day1_1.txt'
with open(FILEPATH) as f:
    code_list = []
    raw = f.readlines()
    lines = [i.strip('\n') for i in raw]
    for line in lines:
        get_code(line, code_list)
    
    print(f'CODE SUM: {sum(code_list)}')
