#importing random function for later
import random

#importing time function for later
import time

#choosing the secret number
print ("What is the secret number between 1-10?")
print ("write it down somewhere, or memorize it")

time.sleep(3)

guesses = []

answer = ("N/A")

print ("I hope you have your number ready!")

time.sleep(2)

#guessing the secret number
while answer != ("Y"):
    guess = random.randint(1,10)
    if (guess) not in guesses:
        print (guess)
        print ("Is this it?")
        print ("Enter Y/N")
        answer = input()
        answer = answer.upper()
        guesses.append(guess)
#finishing script off
print ("Yay!")
time.sleep(2)
