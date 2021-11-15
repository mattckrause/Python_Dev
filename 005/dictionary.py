numb_dict = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}
conv_numb = ""
raw_numb = input("Enter Phone Number: ") + " "

for numb in raw_numb:
    conv_numb += numb_dict[numb]

print(conv_numb)