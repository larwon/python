1.
a = int(input("첫번째 숫자를 입력해주세요."))
b = int(input("두번째 숫자를 입력해주세요."))

if a > b:
    print(">")
elif a == b:
    print("==")
else:
    print("<")


2.
a = int(input("시험성적을 입력해주세요 : "))
if 90 <= a <= 100:
    print("A")
elif 80 <= a <= 89:
    print("B")
elif 70 <= a <= 79:
    print("C")
elif 60 <= a <=69:
    print("D")
else:
    print("F")


3.
a = int(input("연도를 입력해주세요"))

if ((a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)):
    print(1)
else:
    print(0)


4.
a = int(input("x축을 입력해주세요 : "))
b = int(input("y축을 입력해주세요 : "))

if (a > 0 and b > 0):
    print("Quadrant 1")
elif (a < 0 and b > 0):
    print("Quadrant 2")
elif (a < 0 and b < 0):
    print("Quadrant 3")
else:
    print("Quadrant 4")




