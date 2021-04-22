# 1.
import random


a_list = []


a = random.randrange(1, 101)
a_list.append(a)
a = random.randrange(1, 101)
a_list.append(a)
a = random.randrange(1, 101)
a_list.append(a)
a = random.randrange(1, 101)
a_list.append(a)
a = random.randrange(1, 101)
a_list.append(a)

print(a_list)

print("최댓값은 :", max(a_list))
print("최솟값은 :", min(a_list))


# 2.
a = [3, 29, 38, 12, 57, 74, 40, 85, 61]
print(max(a))
print(a.index(max(a))+1)

