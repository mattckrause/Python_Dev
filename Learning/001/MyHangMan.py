#Hang man app
#import modules
import random

#declare variables
word_dictionary = {1:"Cat", 2:"Dog", 3:"Bird", 4:"Fish", 5:"Lizard"}
current_game_word = word_dictionary[random.randint(1,5)].lower()
word_length = len(current_game_word)
correct_guess = ""
incorrect_guess = ""
attempts = 1
game_status = "in progress"
user_guess = " "

#functions
def check_guess(user_guess):
	if user_guess in correct_guess or user_guess in incorrect_guess:
		print("You already guessed that letter try again")
	else:
		if user_guess in current_game_word:
			update_correct(user_guess)
			advance_round()
		else:
			update_incorrect(user_guess)
			advance_round()

def update_correct(letter):
	global correct_guess
	correct_guess += letter
	print("Correct, the word so far: "+ correct_guess)

def update_incorrect(letter):
	global incorrect_guess
	incorrect_guess += letter + " "
	print("Wrong, your incorrect guesses so far: "+ incorrect_guess)

def advance_round():
	global attempts
	attempts += 1
	print("You have " + str(11-attempts) + " attempts left")

#main
print("Welcome to Hangman!")
print("The word is "+ str(word_length) + " letters long")
print("You have 10 attempts to guess the word")
print("the word is " + current_game_word)

while attempts < 11 and game_status != "won":
	user_guess = input("Guess a letter: ").lower()
	if user_guess is None:
	#if len(user_guess) > 1 or user_guess is None:
		print("Please enter only one letter")
	else:
		check_guess(user_guess)
