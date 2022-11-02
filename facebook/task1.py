# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message "111" would give 3, since it could be decoded as "aaa", "ka", and "ak".

# You can assume that the messages are decodable. For example, "001" is not allowed.

en_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

char_num_map = {
    char: num for char, num in enumerate(en_chars, 1)
}


def main(code: str) -> int:
    previous_num = 1
    current_num = 1
    for i in range(1,len(code)):
        available_conditions = any(
            (
                code[i-1]=='1' and
                code[i] in  map(str, (range(1,10))),
                code[i-1]=='2' and
                code[i] in map(str, range(1,7)),
            )
        )
        if available_conditions:
            new_num = previous_num + current_num
        else:
            new_num = current_num

        previous_num = current_num
        current_num = new_num
    return current_num


print(main("22"))
print(main("111"))
print(main("1111"))
