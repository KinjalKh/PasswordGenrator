#!/usr/bin/python3
from logic import main
import tkinter as tk
root = tk.Tk()

# setting the windows size
root.title(" Password Genrator ")
root.geometry("540x300")

# declaring string variable
# for storing values
prefix_var = tk.StringVar()
length_passwd_var = tk.IntVar()
small_char_var = tk.BooleanVar()
capital_char_var = tk.BooleanVar()
number_char_var = tk.BooleanVar()
special_char_var = tk.BooleanVar()
output_var = tk.StringVar()


def submit():
    prefix = prefix_var.get()
    length_passwd = length_passwd_var.get()
    small_char = small_char_var.get()
    capital_char = capital_char_var.get()
    number_char = number_char_var.get()
    special_char = special_char_var.get()
    output_char = main(prefix, length_passwd, small_char,
                       capital_char, number_char, special_char)

    if __name__ == "__main__":
        print("Prefix is : " + prefix)
        print("Length is : ", length_passwd)
        print("Small char : ", small_char)
        print("Capital char : ", capital_char)
        print("number_char : ", number_char)
        print("special_char: ", special_char)
        print("output char: ", output_char)

    output_var.set(output_char)


# creating a label using widget Label
# prefix
prefix_label = tk.Label(root, text='Prefix:',
                        font=('calibre', 10, 'bold'))
prefix_entry = tk.Entry(root, textvariable=prefix_var, width=10,
                        font=('calibre', 10, 'normal'))

# length_passwd
length_passwd_label = tk.Label(root, text='Password Length:',
                               font=('calibre', 10, 'bold'))
length_passwd_entry = tk.Entry(root, textvariable=length_passwd_var, width=10,
                               font=('calibre', 10, 'normal'))
length_passwd_entry.insert(0, 2)

# small char
small_char_label = tk.Label(root, text='Small Characters [a,b,c]',
                            font=('calibre', 10, 'bold'))
small_char_entry = tk.Checkbutton(
    root, variable=small_char_var, onvalue=True, offvalue=False,)

# capital_char
capital_char_label = tk.Label(root, text='Capital Characters [A,B,C]',
                              font=('calibre', 10, 'bold'))
capital_char_entry = tk.Checkbutton(
    root, variable=capital_char_var, onvalue=True, offvalue=False,)

# number_char
number_char_label = tk.Label(root, text='Numbers [1,2,3]',
                             font=('calibre', 10, 'bold'))
number_char_entry = tk.Checkbutton(
    root, variable=number_char_var, onvalue=True, offvalue=False,)

# special_char
special_char_label = tk.Label(root, text='Special Characters [/,?,#]',
                              font=('calibre', 10, 'bold'))
special_char_entry = tk.Checkbutton(
    root, variable=special_char_var, onvalue=True, offvalue=False,)

# output
output_label = tk.Label(root, text='Genrated passwd: ',
                        font=('calibre', 10, 'bold'))
output_entry = tk.Entry(root, textvariable=output_var, width=28,
                        font=('calibre', 10, 'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root, text='Submit', command=submit)

# placing the label and entry in
# the required position using place
label_hight = 10
label_width = 10
entry_width = 260


def label_hight_increment(label_hight):
    label_hight += 30
    return label_hight


# method
prefix_label.place(x=label_width, y=label_hight)
prefix_entry.place(x=entry_width, y=label_hight)

label_hight = label_hight_increment(label_hight)
length_passwd_label.place(x=label_width, y=label_hight)
length_passwd_entry.place(x=entry_width, y=label_hight)

label_hight = label_hight_increment(label_hight)
small_char_label.place(x=label_width, y=label_hight)
small_char_entry.place(x=entry_width, y=label_hight)

label_hight = label_hight_increment(label_hight)
capital_char_label.place(x=label_width, y=label_hight)
capital_char_entry.place(x=entry_width, y=label_hight)

label_hight = label_hight_increment(label_hight)
number_char_label.place(x=label_width, y=label_hight)
number_char_entry.place(x=entry_width, y=label_hight)

label_hight = label_hight_increment(label_hight)
special_char_label.place(x=label_width, y=label_hight)
special_char_entry.place(x=entry_width, y=label_hight)

label_hight = label_hight_increment(label_hight)
sub_btn.place(x=entry_width-40, y=label_hight+10)

label_hight = label_hight_increment(label_hight)
output_label.place(x=label_width, y=label_hight + 30)
output_entry.place(x=entry_width-60, y=label_hight + 30)

# performing an infinite loop
# for the window to display
root.mainloop()
