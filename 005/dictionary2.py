emoji = {
    ":)": "😊",
    ":(": "😢"
}

read_input = input(">")

words = read_input.split(" ")
output = ""
for word in words:
    output += emoji.get(word, word) + " "

print(output)