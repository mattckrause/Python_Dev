def find_max(list):
    max = list[0]
    for number in list:
        if number > max:
            max = number
    return max

def find_min(list):
    min = list[0]
    for number in list:
        if number < min:
            min = number
    return min

def find_average(list):
    list_count = len(list)
    total = 0
    for number in list:
        total += number
    return total/list_count