from random import *

a = [1234, 4567, 7890]
b = choice(a)
print("정답 : " + str(b))

number = ""

while True:
    succed = True
    for x in str(b):
        if x in number:
            print(x, end="")
        else:
            print("_", end="")
            succed = False
    if succed:
        print("Success")
        break
    numbers = input("숫자를 입력해주세요 : ")
    if numbers not in number:
        number += numbers
    if numbers in str(b):
        print("Correct")
    else:
        print("Wrong")