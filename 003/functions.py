
# Functions/loops/random/file output - day 3


import random

array = []
file = "C:/temp/pytest.txt"
# functions


def func(a, b):
    while a <= b:
        array.append(random.randint(1, 100000))
        a = a+1
    return


func(1, 1000)
sort = sorted(array)

print(f"writing data to {file}")
print(sort)
