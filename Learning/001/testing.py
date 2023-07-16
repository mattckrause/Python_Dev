word = "test"
a = "t"
guess = {0:"_", 1:"_", 2:"_", 3:"_"}
final_word = ""

def build_word(var):
    global final_word
    for i in var:
        print(i)
        final_word += var[i]

for i, ltr in enumerate(word):
    if ltr == a:
        guess.update({i:ltr})
build_word(guess)
print(final_word)