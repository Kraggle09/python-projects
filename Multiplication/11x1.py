import random
from time import sleep

print ("Generating problem")

sleep(1)

first = random.randint(1, 9)
second = random.randint(1, 9)
multipliedby = random.randint(1, 9)
firstandsecond = (str(first) + str(second))
print(firstandsecond)
answer = (firstandsecond * multipliedby)
print("What is:", firstandsecond, "x", multipliedby, "?")

user = int(input("Answer: "))

sleep(1)

if user == answer:
    print("Correct!", firstandsecond, "x", multipliedby, "is", str(answer) + "!")
else:
    print("Sorry, that's not it. The correct answer is", str(answer) + ".")

sleep(1)

print("Ending program!")

sleep(2)
