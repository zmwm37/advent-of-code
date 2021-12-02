measurements = [int(i) for i in open('day1-data.txt').read().split()]
# Part 1
def count_increase(measurements):
    '''
    Count the numbers of times the ith measurement is higher than the ith -1 
    measurement.
    '''
    increase_count = 0
    previous_depth = None
    for measurement in measurements:
        if previous_depth:
            if measurement > previous_depth:
                increase_count += 1
        previous_depth = measurement
    return increase_count

# Part 2
def count_window_increase(measurements, window_size = 3):
    '''
    Count the number of times the sum of 3 consecutive measurements 
    (i, i+1, i +2) are greater than the sum of the prior measurement and the
    first two measurements in the current sum (i-1, i, i+1).
    '''
    increase_count = 0
    previous_sum = None
    for i in range(len(measurements) - (window_size - 1)):
        current_sum = sum(measurements[i:i + window_size])
        if previous_sum:
            if current_sum > previous_sum:
                increase_count += 1
        previous_sum = current_sum
    return increase_count
