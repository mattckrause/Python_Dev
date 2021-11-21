import random

def createNumber():
    answer = random.randint(1000,10000)
    return str(answer)


def GetInput():
    guess = input("Enter a 1 digit number: ")
    return guess


def check(game_number,guess):
    cowbull = [0,0]
    for i in range(len(game_number)):
        if game_number[i] == guess[i]:
            cowbull[1]+=1
        else:
            cowbull[0]+=1
    return cowbull


#Main
guess_count = 0
game_number = createNumber()
number = 0

while (number != game_number):
    number = GetInput()
    num_check = check(game_number, number)
    print(game_number)
    print(number)
    print(num_check)
    # print(check)
    guess_count += 1

print(f"Congratulations, you guessed the number. It took you {guess_count} guesses!")