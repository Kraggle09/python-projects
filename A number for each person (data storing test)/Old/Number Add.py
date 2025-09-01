#importing sleep module
from time import sleep

#importing importlib for the pullRequest variable
import importlib

done = False

while done == False:
    #asking if user would like to PULL or ADD a number
    print("Would you like to PULL, or ADD a number?")
    sleep(0.5)
    print("Please type PULL, or ADD")
    sleep(1)
    answer = input("Answer: ")
    


    #scanning user input
    if answer == "PULL":
        #asking user who's number they'd like to pull
        print("Ok, who's number would you like to pull?")
        sleep(0.5)
        print("Please enter the person(who's number you'd like to pull)'s name")
        sleep(1)
        pullRequest = input("Answer: ")
        #getting module that matches pullRequest
        mymodule = importlib.import_module(pullRequest)
        pulledNumber = (mymodule.number)
        #fake scanning
        print("Scanning...")
        sleep(1)
        #displaying pulled number
        print("It looks like " + pullRequest + "'s number is...")
        sleep(1)
        print(pulledNumber)
        sleep(1)
        print("Shutting down program in 10 seconds")
        sleep(10)
        #shutting down program
        print("Shutting down...")
        sleep(0.5)
        exit()

    if answer == "ADD":
        print("Ok, what's your name?")
        sleep(0.5)
        print("Please enter your name")
        sleep(1)
        name = input("Answer: ")
        sleep(1)
        print("Ok " + name + ", what's your number?")
        sleep(1)
        number = input("Answer: ")
        sleep(1)
        print("Ok, so your name is " + name + ", and your number is " + number + "!")
        sleep(1)
        print("Saving data to servers, this might take a bit...")
        sleep(1)
        newFile = open(name + ".py", "w")
        newFile.write("number = '" + number + "'")
        newFile.close
        print("Data saved!")
        sleep(1)
        print("Shutting down program in 5 seconds. IMPORTENT! DON'T ABORT!")
        sleep(5)
        print("Shutting down...")
        sleep(0.5)
        exit()

    if answer != "ADD":
        if answer != "PULL":
            print("Sorry, that's not a valid command. Please try again")
            sleep(2)
