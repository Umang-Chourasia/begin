import random
number = random.randint(1,100)
print("\n\nOne number is generated between 1 to 100.")
guess = int(input("Guess the number: "))
counter = 1
while guess != number:
    if guess < number:
        print("Guess higher.")
    else:
        print("Guess lower.")
    guess = int(input("Guess the number: "))
    counter += 1
print("***Jackpot***")
print("You guessed the number in: ",counter,'turns.')


