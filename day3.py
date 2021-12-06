# Part 1 - Calculate epsilon and gamma rates
import numpy as np

input_data = [i for i in open('day3-data.txt').read().split()]

def calculate_rate(input_data, rate_type = 'gamma'):
    '''
    '''
    bit_array = np.zeros((len(input_data), len(input_data[0])))

    for i, row in enumerate(input_data):
        for j, col in enumerate(row):
            if col == '1':
                bit_array[i][j] = 1

    bits = [str(int(i)) for i in np.rint(np.mean(bit_array, axis = 0))] 
    if rate_type == 'gamma':
        rv = int(''.join(bits), 2)
    elif rate_type == 'epsilon':
        switch_bits = [str(abs(int(i) - 1)) for i in bits]
        rv = int(''.join(switch_bits), 2)
    
    return rv

print(calculate_rate(input_data) * 
    calculate_rate(input_data, rate_type = 'epsilon'))
