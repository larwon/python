# 1.
list = ["1:닥터 스테리인지", "2:스플릿", "3:럭키"]
print(list)


# 2.
list = [{"닥터 스트레인" : {"36.6", "7.7"}},
        {"스플릿" : {"18.8", "8.1"}},
        {"럭키" : {"12.7", "7.6"}}]
print(list[2])
print(list[1].values())


# 3.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)


# 4.
nums = [1, 2, 3, 4, 5, 6]
print("최댓값은 :", max(nums))
print("최솟값은 :", min(nums))


# 5.
nums = [2, 3, 1, 7, 10, 4, 5, 8]
nums.sort()
print(nums)
nums.reverse()
print(nums)


# 6.
close = [10000, 10500, 10300, 10700, 11100]
count = len(close)
sum1 = sum(close)
avg = sum1 / count
print(avg)


# 7.
data = ['a', 'b', 'c', 'd', 'e']
print(type(data))
data = tuple(data)
print(type(data), data)


# 8.
nums = [1, 2, 3, 4, 5]
nums.remove(4)
nums.remove(5)
print(nums)


# 9.
item = ['00600', '034560', '003540', '039490']
mystr = ";".join(item)
print(mystr)








