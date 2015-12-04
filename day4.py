# Day 4: The Ideal Stocking Stuffer

import hashlib

def calc_lowest_zero_hash(input, num_zeroes):
    zero_matcher = '0'*num_zeroes
    curr_num = -1
    while True:
        curr_num += 1
        m = hashlib.md5()
        m.update(input + str(curr_num))

        if (m.hexdigest()[:num_zeroes] == zero_matcher):
            return curr_num


print calc_lowest_zero_hash('bgvyzdsv', 5)
print calc_lowest_zero_hash('bgvyzdsv', 6)
