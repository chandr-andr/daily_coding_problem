# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

from functools import reduce


def main(arr: list):
    res_arr = []
    for idx in range(len(arr)):
        new_arr = arr[idx + 1:] + arr[:idx]
        res_arr.append(
            reduce(lambda x, y: x*y, new_arr),
        )
    return res_arr


print(main([1, 2, 3, 4, 5]))  # [120, 60, 40, 30, 24]
