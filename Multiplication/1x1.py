import random
from time import sleep

print ("Generating problem")

sleep(1)

first = random.randint(1, 9)
multipliedby = random.randint(1, 9)
answer = (first * multipliedby)
print("What is:", first, "x", multipliedby, "?")

user = int(input("Answer: "))

sleep(1)

if user == answer:
    print("Correct!", first, "x", multipliedby, "is", str(answer) + "!")
else:
    print("Sorry, that's not it. The correct answer is", str(answer) + ".")

sleep(1)

print("Ending program!")

sleep(2)
