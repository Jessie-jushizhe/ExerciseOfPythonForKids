import random
guessestaken = 0
number = random.randint(1, 20)
print("Guess a number between 1 and 20, you will have 10 chances in all.")

i = int(input())

while guessestaken < 10:

    guessestaken = guessestaken + 1
    if i < number:
        print("Too low. Try again.")
        i = int(input())

    if i > number:
        print("Too high. Try again.")
        i = int(input())

    if i == number:
        break

if i == number:
    print("Congratulations:)")

if i != number:
    print("Sorry:(")

