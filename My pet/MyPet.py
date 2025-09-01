from time import sleep
from random import randint

print("Have you played before?")
sleep(0.5)
answer = input("Y/N ")
sleep(0.5)
if answer == "N":
    print("Ok, heres how to play:")
    print("You can do a number of things with your pet, including play, feed, teach, and others")
    print("You pet has 4 values:")
    print("Sleep, Hunger, Happiness, and knowledge")
    print("As time goes on, these values will go down. They will go down quicker if you do things like play, or teach.")
    print("If a value is low for too long (excluding knowledge), you pet will die, or leave you, depending on what value is too low")
    print("You can check the commands with the command 'commands'")
    print("Hope this helps!")
    answer = input("Ready to play? Y if ready: ")
print("OK, what would you like to name your pet?")
name = input("Name: ")
sleep(0.5)
print("Ok, now just wait a for about 30 seconds for " + name + " to be born...")
sleep(3)
print(name + " was born!")
sleep(0.5)

gone = False
hunger = 0
happiness = 0
sleep = 0
knowledge = 0

while gone == False:
    print("What would you like to do?")
    answer = input()
    if answer == "commands":
        print("The commands are:")
        print("'feed': Starts feeding process")
        print("'play': Starts the playing process")
        print("'sleep': Turns out the lights, causing pet to fall asleep")
        print("'wake': Turns on the lights, causing pet to wake up")
        print("'teach': Starts the teaching process")
        print("'exit': Ends the program")
        print("More commands coming soon!")
    elif answer == "feed":
        print("Feed")
    elif answer == "play":
        print("Play")
    elif answer == "sleep":
        print("Sleep")
    elif answer == "wake":
        print("Wake")
    elif answer == "teach":
        print("Teach")
    elif answer == "exit":
        exit()
    else:
        print("Unknown command, please try again")

sleep(3)
