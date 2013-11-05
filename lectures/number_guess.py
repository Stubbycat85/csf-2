import random
n = random.randint(1,100)

guessed = False

while (not guessed):
	guess = raw_input("Enter a guess: ")
	guess = int(guess)
	if (guess > n):
		print "Too high!"
	elif (guess < n):
		print "Too low!"
	else:
		print "You got it!"
		guessed = True
