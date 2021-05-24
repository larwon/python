# 157.
list = ['dog', 'cat', 'parrot']
for i in list:
    print(i[0].upper() + i[1:])


# 158.
list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in list:
  split = i.split(".")
  if (split[1] == "h") or (split[1] == "c"):
    print(i)
