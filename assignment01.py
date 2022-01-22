# Robert "Andy" Stockwell
# CIDM 6330 Assignment 01
# Roman numerals Kata

from unicodedata import digit


def roman(number):
    roman_num = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C",
                 500: "D", 1000: "M"}  # Set Roaman & Arabic Values
    roman = ""

    while number > 0:
        value_place = 10 ** (len(str(number))-1)
        # print(f"value_place = {value_place}")
        num = number-(number % value_place)
        # print(f"num = {num}")
        digit = num//value_place
        if digit < 4:
            roman += roman_num[num//digit] * digit
        elif (digit+1) % 5 == 0:
            roman += roman_num[num//digit] + \
                roman_num[(digit+1) * value_place]
        elif digit % 5 == 0:
            roman += roman_num[num]
        elif digit < 10:
            roman += roman_num[5*value_place] + \
                (roman_num[num//digit]*(digit % 5))
        value_place = value_place//10
        number -= num
    return roman


my_numbers = (1, 5, 10, 50, 100, 500, 1000, 354,
              214, 99, 156, 1977, 1995, 2018)
for i in my_numbers:
    print(f"{i} = {roman(i)}")

# my_roman_num = roman(300)
# print(f"Roman = {my_roman_num}")
