from time import sleep
import json

try:
    with open('data.json', 'r') as file:
        data = json.load(file)
except (FileNotFoundError, json.decoder.JSONDecodeError):
        file = open('data.json', 'w')
        file.write("{}")
        file.close()
        with open('data.json', 'r') as file:
            data = json.load(file)

while True:
    print("Would you like to pull or add a number?")
    answer = input("Pull or Add: ")

    if answer.lower() == "pull":
        print("Ok, who's number would you like to pull?")
        name = input("Name: ")
        try:
            print(f"{name.capitalize()}'s number is {data[name.lower()]}.")
        except KeyError:
            print(f"{name.capitalize()} doesn't have a number stored yet.")
        exit()
    elif answer.lower() == "add":
        print("Ok, what's your name?")
        name = input("Name: ")
        try:
            confirmation = str
            while confirmation != "n" and confirmation != "y":
                print(f"Hi {name.capitalize()}, your current number is {data[name.lower()]}. Are you sure you want to replace it?")
                confirmation = input("Y/N: ")
                if confirmation.lower() == "n":
                    exit()
                elif confirmation.lower() != "y":
                    print("That's not a valid answer, please type Y or N.")
        except KeyError:
            pass
        print(f"Ok {name.capitalize()}, what's your number?")
        number = int(input("Number: "))
        print("Saving number...")
        data[name.lower()] = number
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
        exit()
    else:
        print("Sorry, that's not a valid command. Please type pull or add (case insensitive).")