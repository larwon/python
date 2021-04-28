'''
# 71.
my_variable = ()
print(type(my_variable))


# 72.
movie_rank = ('닥터스트레인지', '스플릿', '럭키')
print(movie_rank)


# 73.
my_tuple = (1)
print(my_tuple)
print(type(my_tuple))

my_tuple = (1, )
print(my_tuple)
print(type(my_tuple))
하나의 데이터가 저장되는 경우, 아래와 같이 쉼표를 입력해만 합니다.


# 74.
t = 1, 2, 3, 4
print(type(t))
원칙적으로 튜플은 괄호와 함께 데이터를 정의해야 하지만, 사용자 편의를 위해 괄호 없이도 동작합니다.



# 75.
t = ('a', 'b', 'c')
t[0] = 'A'
print(t)
튜플의 값은 변경할 수 없기 때문에, 리스트와 달리 아래 코드는 동작하지 않습니다.


# 76.
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)


# 77.
a = []
for i in range(2, 100, 2):
    a.append(i)
print(tuple(a))
'''
