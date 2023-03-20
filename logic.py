#!/usr/bin/python3
from random import choice
from list_of_char import *


def main(prefix, length_passwd, small_char, capital_char, number_char, special_char):

    def prefix_check(prefix):
        if len(prefix) == 0:
            return ""
        else:
            return prefix

    def len_of_passwd(len_of_passwd):  # paasword length handler
        # if user put blank defalut value applied
        if len_of_passwd == 0 or len_of_passwd > 100:
            len_of_passwd = 20
        return int(len_of_passwd) - len(prefix)

    def random_char(random_list):
        random_list.clear()
        if small_char == True:
            random_list.append(small_char_list)

        if capital_char == True:
            random_list.append(capital_char_list)

        if number_char == True:
            random_list.append(number_char_list)

        if special_char == True:
            random_list.append(special_char_list)

        return random_list

    def passwd_gernat(pd, length, random_list):
        random_password = ""

        if len(random_list) == 0:
            return "Please select any checkbox"
        else:
            for i in range(length):
                random_char = choice(choice(random_list))
                random_password += random_char
            return pd + random_password

    passwd = passwd_gernat(prefix_check(prefix), len_of_passwd(
        length_passwd), random_char(random_char_list))

    return passwd


if __name__ == "__main__":
    prefix = input("prefix: ")
    length_passwd = int(input("length: "))
    small_char = True
    capital_char = False
    number_char = False
    special_char = True

    print(main(prefix, length_passwd, small_char,
               capital_char, number_char, special_char))
