class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550
        self.state = "main_menu"

    def print_remaining(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def check_resources(self, water, milk, coffee_beans):
        if self.water < water:
            print("Sorry, not enough water!")
            return False
        if self.milk < milk:
            print("Sorry, not enough milk!")
            return False
        if self.coffee_beans < coffee_beans:
            print("Sorry, not enough coffee beans!")
            return False
        if self.cups < 1:
            print("Sorry, not enough cups!")
            return False
        return True

    def buy_coffee(self, choice):
        if choice == "1":
            if self.check_resources(250, 0, 16):
                self.water -= 250
                self.coffee_beans -= 16
                self.cups -= 1
                self.money += 4
                print("I have enough resources, making you a coffee!")
        elif choice == "2":
            if self.check_resources(350, 75, 20):
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.cups -= 1
                self.money += 7
                print("I have enough resources, making you a coffee!")
        elif choice == "3":
            if self.check_resources(200, 100, 12):
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.cups -= 1
                self.money += 6
                print("I have enough resources, making you a coffee!")
        elif choice == "back":
            return

    def fill_machine(self):
        self.water += int(input("Write how many ml of water do you want to add: "))
        self.milk += int(input("Write how many ml of milk do you want to add: "))
        self.coffee_beans += int(input("Write how many grams of coffee beans do you want to add: "))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add: "))

    def take_money(self):
        print(f"I gave you {self.money}")
        self.money = 0

    def process_input(self, user_input):
        if self.state == "main_menu":
            if user_input == "buy":
                self.state = "buy_menu"
            elif user_input == "fill":
                self.fill_machine()
            elif user_input == "take":
                self.take_money()
            elif user_input == "remaining":
                self.print_remaining()
            elif user_input == "exit":
                return False
        elif self.state == "buy_menu":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            self.buy_coffee(user_input)
            self.state = "main_menu"
        return True

    def start(self):
        while True:
            if self.state == "main_menu":
                print("\nWrite action (buy, fill, take, remaining, exit):")
            user_input = input("> ")
            if not self.process_input(user_input):
                break


machine = CoffeeMachine()
machine.start()
