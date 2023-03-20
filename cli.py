#!/usr/bin/python3

# @purp: genrating random pass
# @auth: Kaushal Chaudhry
#!/usr/bin/python3
from logic import main

# prefix, length_passwd, small_char, capital_char, number_char, special_char


def user_input():
    print("\n\t Password Genrator \n")
    prefix = input("enter prefix:\t")
    length_passwd = int(input("enter length:\t"))
    if input("do you want small char? [Y/n]:  ") == "n":
        small_char = False
    else:
        small_char = True

    if input("do you want capital char? [Y/n]: ") == "n":
        capital_char = False
    else:
        capital_char = True

    if input("do you want number char? [Y/n]:  ") == "n":
        number_char = False
    else:
        number_char = True

    if input("do you want special char? [Y/n]: ") == "n":
        special_char = False
    else:
        special_char = True

    return (main(prefix, length_passwd, small_char,
                 capital_char, number_char, special_char))


print("\nGenrated passwd: \t", user_input(), "\n")
