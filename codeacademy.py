'''ext = "tor"

word_game = raw_input("Enter a word:")

if len(word_game) > 0 and word_game.isalpha():
	new_word = word_game.lower()
	first = new_word[0]
	new_word = new_word + first + ext
	new_word = new_word[1:len(new_word)]

print new_word'''

# This program is meant to be an Area Calculator

'''
print "Helo, the calculator is ready"

option = raw_input("What shape would you like to calculate? enter C for Circle or T for Triangle:")
if option == "C":
  radius = float(raw_input("What is the radius?"))
  pi = 3.14159
  area = pi * radius **2
  print str(area)

elif option == "T":
	base = float(raw_input("Please enter the base of the triangle."))
	height = float(raw_input("Please enter the height of the triangle."))
	area = .5 * base * height
	print str(area)

else:
 print "Invalid shape."

print "The program is exiting"  
'''

# Guess the number
from random import randint
from time import sleep
def get_user_guess():
  guess = int(raw_input("Guess a number:"))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum passible value is: %d "%  max_val
  guess = get_user_guess()
  if guess > max_val:
    print("Sorry, but the number you guess must be   smaler than the maximum value")
  else:
    print("Rolling...")
    sleep(2)
    print("First roll is %d "% first_roll)
    sleep(1)
    print("Second roll is %d "% second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print("The total is %d "% total_roll)
    sleep(1)
    print("Results...")
    sleep(1)
    if guess == total_roll:
      print("You won!")
    else:
      print("You lost!")
    
roll_dice(6)