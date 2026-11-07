import random

def main():
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    number = random.randint(1, 100)
    guess = None

    while guess != number:
        guess = int(input("Enter your guess: "))
        if guess < number:
            print("Your guess is too low. Guess again.")
        elif guess > number:
            print("Your guess is too high. Guess again.")
        else:
            print()
            print("Congratulations! You guessed the number correctly!")


if __name__ == "__main__":
    main()
