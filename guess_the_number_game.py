#guess the number game

import random
number=random.randint(1,10)
for i in range(0,3):
    user=int(input("guess the number"))
    if user==number:
        print("Hurray!!")
        print(f"you have guessed the number right its {number}")
        break
if user!=number:
        print(f"your guess is incorrect the number is{number}")
