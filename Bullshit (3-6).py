import random

def generate_number(num_digits):
    digits = list('123456789')
    random.shuffle(digits)
    return ''.join(digits[:num_digits])

def play_game(num_digits):
    number = generate_number(num_digits)
    guesses_left = 20

    print(f"\nI've chosen a {num_digits}-digit number (no 0s, no repeats). You have 20 guesses.\n")

    while guesses_left > 0:
        guess = input(f"Enter your {num_digits}-digit guess ({guesses_left} left): ")

        # Validate input
        if (len(guess) != num_digits or not guess.isdigit() or
            '0' in guess or len(set(guess)) != num_digits):
            print(f"Invalid input. Enter a {num_digits}-digit number with unique digits (no 0s).")
            continue

        bulls = sum(guess[i] == number[i] for i in range(num_digits))
        cows = sum(d in number for d in guess) - bulls

        if bulls == num_digits:
            print(f"🎉 You guessed it! The number was {number}.")
            return
        elif bulls == 0 and cows == 0:
            print("Bullshit!")
        else:
            print(f"{bulls} Bulls, {cows} Cows.")

        guesses_left -= 1

    print(f"Out of guesses! The number was {number}. Better luck next time.")

def ask_num_digits():
    while True:
        try:
            num = int(input("Enter number of digits (3–6): "))
            if 3 <= num <= 6:
                return num
            else:
                print("Please enter a number between 3 and 6.")
        except ValueError:
            print("Enter a valid number.")

# Main loop
print("Welcome to Bulls and Cows!")
num_digits = ask_num_digits()

while True:
    play_game(num_digits)
    again = input("\nDo you want to play again? (y/n): ").strip().lower()

    if again != 'y':
        print("Thanks for playing! Goodbye.")
        break

    same_settings = input("Continue with the same settings? (y/n): ").strip().lower()
    if same_settings != 'y':
        num_digits = ask_num_digits()
