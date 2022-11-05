import re


def user_name():
    pattern = r"[A-Za-z\d]"
    while True:
        name = input("Please enter your name: ")
        if len(name) <= 3 and str(re.match(pattern, name)):
            print("Please enter a valid name: ")
        else:
            print(f"Welcome {name}!")
            return name


def show_menu():
    user_name()
    print(f"""
    *********************************
    It`s time to play some Blackjack!
    *********************************
    """)


def blackjack():
    pass


show_menu()
