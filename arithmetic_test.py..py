import random

def ask_level():
    while True:
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        level = input()
        if level == "1" or level == "2":
            return int(level)
        else:
            print("Incorrect format.")

def generate_task(level):
    if level == 1:
        a, b = random.randint(2, 9), random.randint(2, 9)
        op = random.choice(['+', '-', '*'])
        question = f"{a} {op} {b}"
        answer = eval(question)
    else:
        a = random.randint(11, 29)
        question = f"{a}"
        answer = a ** 2
    return question, answer

def get_user_answer():
    while True:
        ans = input()
        if ans.strip().lstrip('-').isdigit():
            return int(ans)
        else:
            print("Incorrect format.")

def save_result(score, level):
    level_desc = {
        1: "simple operations with numbers 2-9",
        2: "integral squares of 11-29"
    }
    print("Would you like to save your result to the file? Enter yes or no.")
    ans = input().lower()
    if ans in ['yes', 'y']:
        print("What is your name?")
        name = input()
        line = f"{name}: {score}/5 in level {level} ({level_desc[level]}).\n"
        with open("results.txt", "a") as f:
            f.write(line)
        print('The results are saved in "results.txt".')

def main():
    score = 0
    level = ask_level()
    for _ in range(5):
        question, correct = generate_task(level)
        print(question)
        answer = get_user_answer()
        if answer == correct:
            print("Right!")
            score += 1
        else:
            print("Wrong!")
    print(f"Your mark is {score}/5.")
    save_result(score, level)

if __name__ == "__main__":
    main()
