"""
while condition == true:
    do this
    break
"""

loop = True

while loop:
    name = input("Insert a word:")
    if name == "stop":
        print("yes stop!!")
        break

while loop:
    password = input("enter the password:")
    if password == "4570":
        print("correct password!!")
    else:
        print("retry!! :(")
        