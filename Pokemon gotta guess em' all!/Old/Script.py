from time import sleep
from random import choice
import Pokemon

print("Welcome to Pokemon: Gotta Guess Em' All!")
sleep(1)
print("The ultimate Pokemon Game Show!")
sleep(1)
print("Do you already know how to play?")
sleep(1)
played = input("Y or N: ")
sleep(1)
if played == "N":
    print("Ok, I will show you how to play!")
    sleep(1)
    print("Each round, you will be given a pokemon's name. ")
    sleep(1)
    print("You will then have to guess which that pokemon's type is.")
    sleep(1)
    print("For example, Charmander is the Lizard Pokemon!")
    sleep(1)
    print("Don't worry though, you'll be given 4 options.")
    sleep(1)
elif played == "Y":
    print("Ok then, let's start the game!")
    sleep(1)

print("Choosing Pokemon...")
sleep(3)
#pokemon = choice(Pokemon.pokemon)
pokemon = "Charizard"
print("The Pokemon is...")
sleep(1)
print(pokemon + "!")
sleep(1)
if pokemon == "Charizard":
    print("Is Charizard the Lizard, Flame, Dragon, or the Big Lizard Pokemon?")
    sleep(1)
    answer = 
