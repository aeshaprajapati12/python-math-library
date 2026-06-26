import random

number = random.randint(1, 5)
score = 0

print("------------------ Guess the Number Game --------------------")
print("Guess a number between 1 and 5")
print("You have 5 chances.\n")

for chance in range(1, 6):
    guess = int(input(f"Chance {chance}: Enter your guess: "))

    if guess == number:
        score += 1
        print("Correct Guess!")
        print("Score:", score)
        break
        print("\n")
    else:
        score -= 1
        print("Wrong Guess!")
        print("Score:", score)
        print("\n")

if guess != number:
    print("\nGame Over!")
    print("The correct number was:", number)
    print("\n")