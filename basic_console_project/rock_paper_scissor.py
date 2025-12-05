import random

class RockPaperScissors:
    def __init__(self, choice):
        self.choice = choice

    def rock_paper_scissor(self):
        return random.choice(self.choice)
    

if __name__ == "__main__":
    options = {1: "Rock", 2: "Paper", 3: "Scissors"}

    print("="*120)
    print("="*120)
    print("="*50, " Rock Paper Scissors ", "="*50)
    print("="*120)
    print("="*120)

    while True:
        print("\nSelect between 1-3:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("0. Exit")

        try:
            user_choice = int(input("Enter your choice : "))
        except Exception as message:
            print("Error:", message)
            continue

        if user_choice == 0:
            print("\nThanks for playing! Goodbye ")
            break

        if user_choice not in [1, 2, 3]:
            print("Invalid choice! Please choose 1, 2, 3, or 0.")
            continue

        # Computer choice
        game = RockPaperScissors(["Rock", "Paper", "Scissors"])
        computer_choice = game.rock_paper_scissor()

        print(f"\nYou chose     : {options[user_choice]}")
        print(f"Computer chose: {computer_choice}")

        # Determine winner
        user = options[user_choice]
        comp = computer_choice

        if user == comp:
            print("Result: It's a Tie!")
        elif (
            (user == "Rock" and comp == "Scissors") or
            (user == "Paper" and comp == "Rock") or
            (user == "Scissors" and comp == "Paper")
        ):
            print("Result: You Win!")
        else:
            print("Result: Computer Wins!")

        print("-"*120)
