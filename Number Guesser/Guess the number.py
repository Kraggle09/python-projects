import random

#importing time function for later
import time

#choosing the secret number
print ("Choosing secret number secret number between 1-10...")

time.sleep(3)

Secret_number = random.randint(1,10)

guesses = []

print ("I hope your ready!")

time.sleep(2)

print (Secret_number)

#guessing the secret number
guess = input()
if guess == Secret_number:
    print ("Yay! Thats it!")
else:
    print ("Sorry, thats not it")
time.sleep(2)
