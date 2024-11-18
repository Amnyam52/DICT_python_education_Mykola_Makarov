import random


def main():

    try:
        num_friends = int(input("Enter the number of friends joining (including you):\n> "))
        if num_friends <= 0:
            print("No one is joining for the party")
            return
    except ValueError:
        print("Invalid input")
        return


    friends = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_friends):
        name = input("> ")
        friends[name] = 0



    try:
        total_amount = float(input("Enter the total amount:\n> "))
    except ValueError:
        print("Invalid input")
        return

    split_amount = round(total_amount / num_friends, 2)
    for name in friends:
        friends[name] = split_amount



    lucky_answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n> ')
    if lucky_answer == "Yes":
        lucky_friend = random.choice(list(friends.keys()))
        print(f"{lucky_friend} is the lucky one!")

        split_amount = round(total_amount / (num_friends - 1), 2)
        for name in friends:
            friends[name] = split_amount if name != lucky_friend else 0
    else:
        print("No one is going to be lucky")

    print(friends)


if __name__ == "__main__":
    main()

