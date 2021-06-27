import random

for i in range(0,100):
    magic_num = random.randrange(0, 10)
    print(magic_num)
    if magic_num == 0:
        print("Magic number is : " + str(magic_num))
        break
    else:
        continue



"""

magic_num = random.randrange(0, 10)

guess_num = input("Input your guess here: ")

    if magic_num == guess_num:
        print('Congrats!! You have won!!!')
    else:
        print("Incorrect guess... Run the program again if you want to try again")
"""
