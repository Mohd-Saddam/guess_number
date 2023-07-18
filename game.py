import random
import time

def intro():
    """
    Introduce the game and ask for the player's name.
    """
    print("May I ask you for your name:")
    name = input()

    # Display game instructions
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(0.5)
    print("Go ahead. Guess!")

    return name

def pick(name):
    """
    Play the number guessing game.
    """
    guessesTaken = 0

    # Continue until the player runs out of guesses or guesses correctly
    while guessesTaken < 6:
        # Insert a small delay before prompting for a guess
        time.sleep(0.25)
        enter = input("Guess: ")

        try:
            # Convert the entered value into an integer
            guess = int(enter)

            # Check if the guess is within the valid range
            if 1 <= guess <= 200:
                # Increment the number of guesses taken
                guessesTaken += 1

                if guessesTaken < 6:
                    # Provide feedback on the guess (too low, too high, or correct)
                    if guess < number:
                        print("The guess of the number that you have entered is too low")
                    elif guess > number:
                        print("The guess of the number that you have entered is too high")
                    else:
                        # If the guess is correct, prompt for the next round
                        time.sleep(0.5)
                        print("Try Again!")

                elif guess == number:
                    break
            else:
                # If the guess is out of range, prompt the user to enter a valid number
                print("Silly Goose! That number isn't in the range!")
                time.sleep(0.25)
                print("Please enter a number between 1 and 200")
        except ValueError:
            # Handle the case when a non-numeric value is entered as a guess
            print(f"I don't think that {enter} is a number. Sorry")

    if guess == number:
        # Print the number of guesses it took to guess the correct number
        print(f'Good job, {name}! You guessed my number in {guessesTaken} guesses!')
    else:
        # If the user couldn't guess the correct number within 6 attempts, reveal the number
        print(f'Nope. The number I was thinking of was {number}')

while True:
    # Generate a random number between 1 and 200 for the user to guess
    number = random.randint(1, 200)

    # Start the game by introducing the user and the game rules
    name = intro()

    # Begin the game by prompting the user to make guesses
    pick(name)

    # Ask if the user wants to play again; if not, exit the loop and end the game
    print("Do you want to play again? (yes/no)")
    playagain = input().lower()
    if playagain != "yes" and playagain != "y":
        break
