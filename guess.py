guess = int(input("What is your guess?: "))
correct_number = 5
guess_count = 1

while guess != correct_number:
    guess_count += 1
    if guess < correct_number:

        guess = int(input("Wrong answer, you need to guess higher. What is your guess?: "))


print(f"The right answer was {correct_number}. It took you {guess_count} guesses!")