#number guessing game

lowest_num = 1
highest_num = 100
is_running = True
guesses = 0 
score = 0
    
import random
number_to_guess = random.randint(lowest_num, highest_num)



print("---------------------- NUMBER GUESSING GAME ------------------------")
print(f"Welcome to the Number Guessing Game! I'm thinking of a number between {lowest_num} and {highest_num}. Can you guess it?")


while is_running:
    user_guess = input("Enter your guess (or 'q' to quit): ")
    if user_guess.lower() == 'q':
        print("Thanks for playing! Goodbye!")
        print(f"The number was: {number_to_guess}")
        print(f"Your final score: {score} | Total guesses: {guesses}")
        break   
    elif user_guess.isdigit():
        user_guess = int(user_guess)
        guesses += 1
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {guesses} guesses!")
            score += 1
            print(f"Current Score: {score} | Guesses: {guesses}")
            while True:
                choice = input("Enter 'c' to continue or 'q' to quit: ").lower()
                if choice == 'c':
                    number_to_guess = random.randint(lowest_num, highest_num)
                    guesses = 0
                    print(f"Great! I'm thinking of a new number between {lowest_num} and {highest_num}. Can you guess it?")
                    break
                elif choice == 'q':
                    print("Thanks for playing! Goodbye!")
                    print(f"The number was: {number_to_guess}")
                    print(f"Your final score: {score} | Total guesses: {guesses}")  
                    is_running = False
                    break
                else:
                    print("Invalid input. Please enter 'c' to continue or 'q' to quit.")

    elif user_guess.lower() == "":
        print("Please enter a guess or 'q' to quit.")
    else:
        print("Invalid input. Please enter a number or 'q' to quit.")

    
