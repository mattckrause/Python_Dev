input_1 = input("Enter any number: ")
input_2 = input("Enter another number: ")

if int(input_1) > int(input_2):
    print(f"The bigger number is {input_1}")
elif int(input_1) == int(input_2):
    print("You entered the same number...")
else:
    print(f"{input_2} is the bigger number")