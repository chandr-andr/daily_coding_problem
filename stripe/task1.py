# Good morning! Here's your coding interview problem for today.

# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.


def main(nums: list):
    nums.append(0)
    nums.sort()
    if nums[-1] < 0:
        return 1

    for idx, num in enumerate(nums):
        if num < 0:
            continue

        if idx + 1 == len(nums) or nums[idx + 1] - nums[idx] > 1:
            return nums[idx] + 1

    return None


print(main([3, 4, -1, 1])) # 2
print(main([1, 2, 0])) # 3
print(main([-10, -2, 0, 1, 1, 1, 2, 2, 3, 4, 10, 15])) # 5
print(main([0, 2, 3])) # 1
print(main([-5])) # 1
print(main([-1,-2,-60,40,43])) # 1
