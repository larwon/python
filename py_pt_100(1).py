# 11. 이스케이프 문자
# \t, \n
print("a\tb\tc\t")  #\t : 탭
print("a\nb\nc\n")  #\n : 강제개행


# 12. 구분자를 사용한 출력
# sep 인자 사용
print("naver","kakao","samsung", sep=';')


# 13. mystring의 길이를 출력하는 프로그램을 구현하라
print(len("mystring"))


# 14. 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하라
license_plate = "24가 2210"
print(license_plate[4:])


# 15. 문자열 분리
resolution2 = "1920x1080"
width = resolution2[0:4]
height = resolution2[5:]
print("width =", width)
print("height =", height)
