import random

def createNumber():
    answer = random.randint(1000,10000)
    return str(answer)


def GetInput():
    guess = input("Guess the 4 digit number: ")
    return guess


def check(game_number,guess):
    cowbull = [0,0]
    for i in range(len(game_number)):
        if game_number[i] == guess[i]:
            cowbull[0]+=1
        else:
            if game_number.__contains__(guess[i]):
                cowbull[1]+=1
    return cowbull
1

#Main
guess_count = 0
game_number = createNumber()
number = 0

while (number != game_number):
    number = GetInput()
    num_check = check(game_number, number)
    print(f"Your guess of {number} has {num_check[0]} cows and {num_check[1]} bulls")
    guess_count += 1

print(f"Congratulations, you guessed the number. It took you {guess_count} guesses!")