import random

length = int(input("Enter length of the password: "))
if length < 8 or length > 16:
    print("Sorry! The range is not supported.")
    quit()

pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z', 'A', 'B',
        'C', 'D', 'E', 'F', 'G', 'H', 'I',
        'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W',
        'X', 'Y', 'Z', '1', '2', '3', '4',
        '5', '6', '7', '8', '9', '0', '!',
        '@', '#', '$', '%', '^', '&', '*',
        '(', ')', '?', '<', '>', '/', '|']

pwd = ""

for x in range(length):
    pwd += random.choices(pass1)[0]

print(f"Your Password is: {pwd}")