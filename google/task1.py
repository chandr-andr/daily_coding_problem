# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

list_ = [10, 15, 3, 7]

# First solution.
def main(num_list: list, k: int) -> bool:
    for idx, up_num in enumerate(num_list, 1):
        for down_num in num_list[idx:]:
            if up_num + down_num == k:
                return True
    return False


res = main(list_, 17)
print(res)  # True


# Second solution.
def main2(num_list: list, k: int) -> bool:
    hashset = set()
    for num in num_list:
        if k - num in hashset:
            return True
        hashset.add(num)
    return False


res = main2(list_, 17)
print(res)  # True
