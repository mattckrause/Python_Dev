list = [1,2,3,3,4,6,6,7,2]
list = sorted(list)
remove = []
previous = 0
for numb in list:
    if numb == previous:
        print(f"{numb} is a duplicate")
        remove.append(numb)
    else:
        previous = numb
        print(f"new number is {numb}")

for i in remove:
    list.remove(i)

print(list)