import random

#Variables
dict = ["jet", "cat", "bin"]
index = len(dict)
word = dict[(random.randint(0,index - 1))]
max_guess = 10
current_guess = 1
first = "_"
second = "_"
third = "_"
won = False

def check (word,first,second,third):
    current_answer = first+second+third
    if current_answer == word:
        won = True
    else:
        won = False
    return won

print("Welcome to Hangman, try to guess the 3 letter word:")
print(f"{first} {second} {third}")

while current_guess <= max_guess:
    guess = input("Guess a Letter ").lower()
    if word.__contains__(guess):
        if word[0] == guess:
            print("That was a good guess!")
            first = guess
            won = check(word,first,second,third)
            if won == True:
                print("You Won!!!")
                print(f"{first} {second} {third}")
                break
        elif word[1] == guess:
            print("That was a good guess!")
            second = guess
            won = check(word,first,second,third)
            if won == True:
                print("You Won!!!")
                print(f"{first} {second} {third}")
                break
        elif word[2] == guess:
            print("That was a good guess!")
            third = guess
            won = check(word,first,second,third)
            if won == True:
                print("You Won!!!")
                print(f"{first} {second} {third}")
                break
        else:
            print("Nope, try again.")

    print(f"{first} {second} {third}")
    if max_guess - current_guess == 0:
        print("Sorry, you lose...")
    else:
        print(f"{max_guess - current_guess} guesses left")
    current_guess += 1