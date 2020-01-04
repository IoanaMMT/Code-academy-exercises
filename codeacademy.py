'''ext = "tor"

word_game = raw_input("Enter a word:")

if len(word_game) > 0 and word_game.isalpha():
	new_word = word_game.lower()
	first = new_word[0]
	new_word = new_word + first + ext
	new_word = new_word[1:len(new_word)]

print new_word'''

# This program is meant to be an Area Calculator
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