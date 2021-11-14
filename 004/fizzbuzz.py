#my fizz/buzz
# count to 100, if devisible by 5 print fizz, if by 7 print buzz
count_limit = input("How high should Fizz/Buzz go? ")
count = 1
for count in range(int(count_limit)+1):
    if count % 5 == 0 and count % 7 == 0:
        print(f"{count} Fizz Buzz")
    elif count % 5 == 0:
        print(f"{count} Fizz")
    elif count % 7 == 0:
        print(f"{count} Buzz")
    else:
        print(count)
    count += count