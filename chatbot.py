def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")

def remind_name():
    print("Please, remind me your name.")
    name = input()
    print(f"What a great name you have, {name}!")

greet("DICT_Bot", 2024)
remind_name()

def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")

guess_age()

def count():
    print("Now I will prove to you that I can count to any number you want.")
    numbers = int(input())
    for i in range(numbers + 1):
        print(f"{i} !")

count()

def test():
    print("Let's test your programming knowledge.")
    print("What types of data do strings consist of?")
    print("1. float")
    print("2. int")
    print("3. char")
    print("4. bool")

    while True:
        answer = int(input())
        if answer == 3:
            print("Completed, have a nice day!")
            break
        else:
            print("Please, try again.")

test()
print("Congratulations, have a nice day!")
