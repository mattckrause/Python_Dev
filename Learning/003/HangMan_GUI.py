#Hang man app
#import modules
import random
import tkinter

#declare variables
word_dictionary = {1:"Cat", 2:"Dog", 3:"Bird", 4:"Fish", 5:"Lizard", 6:"Girraffe", 7:"Elephant", 8:"Monkey", 9:"Tiger", 10:"Lion"}
guess_dictionary = {}
current_game_word = word_dictionary[random.randint(1,10)].lower()
word_length = len(current_game_word)
correct_guess = ""
incorrect_guess = ""
incorrect_guess_count = 10
attempts = 1
game_status = "in progress"

#functions
def check_guess(user_guess):
	global correct_guess
	if user_guess in correct_guess or user_guess in incorrect_guess:
		print("You already guessed that letter try again")
	elif user_guess == "":
		print("\nPlease enter only one letter\n")
	elif user_guess.isalpha() == False:
		print("\nPlease enter only letters\n")
	elif len(user_guess) > 1:
		print("\nPlease enter only one letter\n")
	else:
		if user_guess in current_game_word:
			print("Correct, guess again:\n") #move this so it doesn't prompt on game winning guess
			update_correct(user_guess)
			check_game_status()
			print_game_status()
		else:
			print("Wrong, try again:\n") #move this so it doesn't promt on a game losing guess
			update_incorrect(user_guess)
			check_game_status()
			print_game_status()
			advance_round()

def check_game_status():
	global game_status
	build_word(guess_dictionary)
	if attempts == incorrect_guess_count:
		game_status = "lost"
		return game_status
	elif correct_guess == current_game_word:
		game_status = "won"
		return game_status
	#elif correct_guess != current_game_word:
	#	game_status = "lost"
	#	return game_status
	else:
		game_status = "in progress"
		return game_status

def print_game_status():
	global correct_guess
	global incorrect_guess
	global word_length
	if game_status == "won":
		print(correct_guess)
		print("\n\n***Congratulations, You won!!")
		return
	elif game_status == "lost":
		print("\n:(\nYou lost, the word was " + current_game_word)
		return
	else:
		print("Game Status:\n")
		print("Your correct guesses so far: " + correct_guess)
		print("Your incorrect guesses so far: " + incorrect_guess)
		return

def build_word(var):
	global correct_guess
	correct_guess = ""
	for i in var:
		correct_guess += var[i]

def build_dictionary():
	global guess_dictionary
	for i in range(0,word_length):
		guess_dictionary.update({i:"_"})

def update_correct(letter):
	global correct_guess
	for i, ltr in enumerate(current_game_word):
		if ltr == user_guess:
			guess_dictionary.update({i:ltr})

def update_incorrect(letter):
	global incorrect_guess
	incorrect_guess += letter + " "

def advance_round():
	global attempts
	attempts += 1
	user_guess = ""
	if attempts >= 1:
		print("\nYou have " + str(11-attempts) + " attempts left\n")
	else:
		return

#main
if __name__ == "__main__":
	print("Welcome to Hangman!\n\n")
	print("The word is "+ str(word_length) + " letters long\n")
	print("You have 10 attempts to guess the word\nGood Luck!\n\n")
	build_dictionary()

	while game_status != "won" and game_status != "lost":
		user_guess = input("Guess a letter: ").lower()
		check_guess(user_guess)
