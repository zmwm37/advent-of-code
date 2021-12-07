# Part 1 - Calculate epsilon and gamma rates
import numpy as np

input_data = [i for i in open('day3-data.txt').read().split()]
# test_data = [i for i in open('day3-example-data.txt').read().split()]

def input_to_array(input_data):
    bit_array = np.zeros((len(input_data), len(input_data[0])))

    for i, row in enumerate(input_data):
        for j, col in enumerate(row):
            if col == '1':
                bit_array[i][j] = 1
    
    return bit_array

def most_common_bit(bit_array):
    # this list comp. alternative approach is about 50% slower accoridng to timeit
    # bit_array = np.array([list(map(int, list(row))) for row in input_data])

    bits = [str(int(i)) for i in np.rint(np.mean(bit_array, axis = 0))] 

    return bits


def calculate_rate(bits, rate_type = 'gamma'):
    '''
    '''
    assert(rate_type in {'gamma', 'epsilon'})
    

    if rate_type == 'gamma':
        rv = int(''.join(bits), 2)
    elif rate_type == 'epsilon':
        switch_bits = [str(abs(int(i) - 1)) for i in bits]
        rv = int(''.join(switch_bits), 2)
    
    return rv


bit_array = input_to_array(input_data)
bits = most_common_bit(bit_array)
print('GAMMA * EPISOLON:', calculate_rate(bits) * 
    calculate_rate(bits, rate_type = 'epsilon'))

# Part 2
# calculate most common bits (from part 1)
bits_array = input_to_array(input_data)

# recursively filter list until one value
# convert bit to integer
def life_support_rating(bit_array, index = 0, match_most_freq = True):
    '''
    Recursively identify most frequent value in the ith column and filter 
    a 2d array based on that value until there is only one element in the array.
    '''
    if len(bit_array) == 1:
        rv =  bit_array
    else:
        if np.mean(bit_array[:, index]) >= 0.5:
            most_freq = 1
        else:
            most_freq = 0

        if match_most_freq:
            new_array = bit_array[bit_array[:, index] == most_freq]
        else:
            new_array = bit_array[bit_array[:, index] != most_freq]
        index += 1
        rv = life_support_rating(new_array, index, match_most_freq)
    
    return rv

oxygen_generator_bits = life_support_rating(bits_array)

oxygen_rating = int(''.join([str(int(i)) for i in oxygen_generator_bits[0]]), 2)

co2_scrubber_bits = life_support_rating(bits_array, match_most_freq = False)
co2_rating = int(''.join([str(int(i)) for i in co2_scrubber_bits[0]]), 2)

print('OXYGEN RATING * CO2 RATING:',oxygen_rating * co2_rating)
    
    