#!/usr/bin/python3
import string

small_char_list = list(string.ascii_lowercase)
capital_char_list = list(string.ascii_uppercase)
number_char_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_char_list = ['~', ':', "'", '+', '[', '\\', '@', '^',
               '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
random_char_list = []

if __name__ == "__main__":
    print("small char", small_char_list)
    print("capital", capital_char_list)
    print("number", number_char_list)
    print("special", special_char_list)
    print("random",random_char_list)
