import json
import random

with open('pokemon.json', 'r') as file:
    pokemonDict = json.load(file)

pokemon = random.choice(list(pokemonDict))

options = pokemonDict[pokemon]['options']
random.shuffle(options)

answer = pokemonDict[pokemon]['answer']

print(f"The Pokemon is {pokemon.capitalize()}!")
print(f"Is {pokemon.capitalize()} the {options[0].capitalize()}, {options[1].capitalize()}, {options[2].capitalize()}, or {options[3].capitalize()} Pokemon?")
guess = input("> ")

if guess.lower() == answer:
    print(f"Correct! {pokemon.capitalize()} is the {answer.capitalize()} Pokemon!")
else:
    print(f"Nope! {pokemon.capitalize()} is the {answer.capitalize()} Pokemon!")