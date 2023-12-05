def parse_input(fp):
    '''
    Read text file where each line is empty or an integer and return dictionary of 
    counts by elf.
    '''
    with open(fp) as f:
        raw = f.readlines()
        lines = [i.strip('\n') for i in raw]
        elf_calories = {}
        cal_counter = 0
        id = 0
        for i, l in enumerate(lines):
            if l == '':
                elf_calories[id] = cal_counter
                cal_counter = 0
                id += 1
            elif i + 1 == len(lines):
                elf_calories[id] = (cal_counter + int(l))
            else:
                cal_counter += int(l)
    return elf_calories

def get_max_cal(elf_calories):
    max_cal = 0
    max_id = None 
    for elf_id, cals in elf_calories.items():
        if cals > max_cal:
            max_cal = cals
            max_id = elf_id
    return (max_id, max_cal)

def get_max_n_cal(elf_calories, top_n=1):
    max_cal = [0] * top_n
    for cals in elf_calories.values():
        if cals > min(max_cal):
            max_cal.append(cals)
            max_cal.sort(reverse=True)
            max_cal.pop()
    return sum(max_cal)



fp = 'day1_data.txt'

elf_calories = parse_input(fp)
print('MAX CALORIES')
elf_id, elf_calories = get_max_cal(elf_calories)
print(f'Elf #{elf_id} has the most calories with {elf_calories} total calories')
n=3
print(f'Top {n} Elf Calories: {get_max_n_cal(elf_calories, n)}')
