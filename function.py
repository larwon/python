x = "awesome" #전역변수

def myfunc():
    x = "Fantastic" #지역변수
    print("Python is " + x)

myfunc()

print("Python is " + x)
