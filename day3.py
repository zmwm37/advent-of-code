# Part 1 - Calculate epsilon and gamma rates
import numpy as np

input_data = [i for i in open('day3-data.txt').read().split()]
# test_data = [i for i in open('day3-example-data.txt').read().split()]

def input_to_array(input_data):
    '''
    Convert input list of bit strings to 2d numpy array.

    Inputs:
        input_data(list): list of bit strings
    
    Outputs:
        bit_array(array): 2d array, where each element is a 0 or 1.
    '''
    bit_array = np.zeros((len(input_data), len(input_data[0])))

    for i, row in enumerate(input_data):
        for j, col in enumerate(row):
            if col == '1':
                bit_array[i][j] = 1
    
    return bit_array

def most_common_bit(bit_array):
    '''
    Calculate whether 1 or 0 is most common value in each column of a 2d array.
    Return most common values as strings for easier manipualtion downstream.
    Note: If 1 and 0 are equally common, returns 0.

    Inputs:
        bit_array(array): 2d array, where each element is a 0 or 1.
    
    Outputs:
        A a list of string representations of 0 or 1.
    '''
    return [str(int(i)) for i in np.rint(np.mean(bit_array, axis = 0))] 


def calculate_rate(bits, rate_type = 'gamma'):
    '''
    Concatenate a list of bits and convert from binary to decimal. If the
    rate_type is epsilon, convert 0s to 1s and 1s to 0s before converting from
    binary to decimal.

    Inputs:
        bits (list): A a list of string representations of 0 or 1 indicating the
            most or least common integer in each column of the bit_array.
        rate_type (string): Gamma if most frequent bits should be used, 
            epsilon if least common bits should be used.

    '''
    assert(rate_type in {'gamma', 'epsilon'})
    
    if rate_type == 'gamma':
        rv = int(''.join(bits), 2)
    elif rate_type == 'epsilon':
        switch_bits = [str(abs(int(i) - 1)) for i in bits]
        rv = int(''.join(switch_bits), 2)
    
    return rv

# Part 2 Function
def life_support_rating(bit_array, index = 0, match_most_freq = True):
    '''
    Recursively identify most frequent value in the ith column and filter 
    a 2d array based on that value until there is only one element in the array.
    Convert the last remaining element from binary to decimal

    Inputs:
        bit_array (array): 2d array, where each element is a 0 or 1.
        index (int): the index of which column of bit_array is being evaluated.
        match_most_freq (bool): Find most frequent integer in column if True,
            find least frequent if False.

    Outputs:
        rv (int): A decimal integer representation of the algorithmically
            determined final binary number.
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

bit_array = input_to_array(input_data)
bits = most_common_bit(bit_array)
print('GAMMA * EPSILON:', calculate_rate(bits) * 
    calculate_rate(bits, rate_type = 'epsilon'))

oxygen_generator_bits = life_support_rating(bit_array)

oxygen_rating = int(''.join([str(int(i)) for i in oxygen_generator_bits[0]]), 2)

co2_scrubber_bits = life_support_rating(bit_array, match_most_freq = False)
co2_rating = int(''.join([str(int(i)) for i in co2_scrubber_bits[0]]), 2)

print('OXYGEN RATING * CO2 RATING:',oxygen_rating * co2_rating)
    
    