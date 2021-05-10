# 122.
score = int(input("학점을 입력해주세요.: "))

if (score > 80 and score <= 100):
    print("A")
elif (score > 60 and score <= 80):
    print("B")
elif (score > 40 and score <= 60):
    print("C")
elif (score > 20 and score <= 40):
    print("D")
else:
    print("E")

    
# 123.
a = input("금액을 입력해주세요: ")

환율 = {"달러": 1167, 
        "엔": 1.096, 
        "유로": 1268, 
        "위안": 171}
num, currency = a.split()
print(float(num) * 환율[currency], "원")
