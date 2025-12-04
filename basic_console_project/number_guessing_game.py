import random

class NumberGuessingGame:
    def __init__(self):
        pass

    def number_generation(self):
        return random.randint(1, 100)
    
if __name__ == "__main__":
    print("="*120)
    print("="*120)
    print("="*48, " Number Guessing Game ", "="*48)
    print("="*120)
    print("="*120)

    game = NumberGuessingGame()
    target = game.number_generation()   # generate random number once

    while True:
        try:
            number = int(input("Enter your number between 1-100 : "))
        except Exception as message:
            print("Error:", message)
            continue

        # Validate input
        if number < 1 or number > 100:
            print("Invalid number! Enter between 1-100.")
            continue

        # Game logic
        if number == target:
            print("Congratulation! You guessed the right number:", target)
            break
        
        elif number > target:
            print("Number is high")

        elif number < target:
            print("Number is low")

    print("="*120)
    print("="*120)
