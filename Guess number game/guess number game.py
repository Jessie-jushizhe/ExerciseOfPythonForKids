import random
guessesTaken = 0

print("Hi! What's your name?")
name = input()

number = random.randint(1,20)
print("Well,'" + name + "' . Now I am thinking of a number between 1 and 20, Please guess.")

while guessesTaken < 6:
    print("Take a guess.")
    guess = int(input())

    guessesTaken = guessesTaken + 1

    if guess < number:
        print("Your guess is too low.")

    if guess > number:
        print("Your guess is too high.")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print("Congratulations! You guessed my number in " + str(guessesTaken) + "guesses.")

if guess != number:
    number = str(number)
    print("Sorry, the number I was thinking of was " + number)