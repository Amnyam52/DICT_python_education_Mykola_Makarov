import random

user_name = input("Enter your name: ").strip()

ratings = {}
try:
    with open("rating.txt", "r") as file:
        for line in file:
            name, score = line.strip().split()
            ratings[name] = int(score)
except FileNotFoundError:
    pass
if user_name not in ratings:
    ratings[user_name] = 0

rating = ratings[user_name]

print(f"Hello, {user_name}")

options_input = input().strip()
if options_input == "":
    options = ["rock", "paper", "scissors"]
else:
    options = options_input.split(",")

print("Okay, let's start")

def determine_outcome(user_choice, computer_choice, options):
    if user_choice == computer_choice:
        return "draw"
    half = len(options) // 2
    user_index = options.index(user_choice)
    losing = options[user_index + 1:user_index + 1 + half]
    if len(losing) < half:
        losing += options[:half - len(losing)]
    if computer_choice in losing:
        return "lose"
    else:
        return "win"

while True:
    user_input = input().strip()
    if user_input == "!exit":
        print("Bye!")
        break
    elif user_input == "!rating":
        print(f"Your rating: {rating}")
    elif user_input in options:
        computer_choice = random.choice(options)
        result = determine_outcome(user_input, computer_choice, options)
        if result == "draw":
            print(f"There is a draw ({computer_choice})")
            rating += 50
        elif result == "win":
            print(f"Well done. The computer chose {computer_choice} and failed")
            rating += 100
        else:
            print(f"Sorry, but the computer chose {computer_choice}")
    else:
        print("Invalid input")

ratings[user_name] = rating

with open("rating.txt", "w") as file:
    for name, score in ratings.items():
        file.write(f"{name} {score}\n")


