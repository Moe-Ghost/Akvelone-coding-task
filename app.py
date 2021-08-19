"""
main code
"""
# reference class to convert
from NumberFormatter import NumberFormatter

# main block
if __name__ == '__main__':
    num_string = input("Enter string of numbers: ")

    if NumberFormatter.validating(num_string) == 1:
        my_generator = NumberFormatter.parse_int(num_string)

        for num in my_generator:
            print(num)
    else:
        print(NumberFormatter.validating(num_string))
