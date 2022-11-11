import re

from deck import suits, ranks, values


def user():
    pattern = r"[A-Za-z\d]"
    while True:
        player = input("Please type in your name: ")
        if len(player) <= 3 and str(re.match(pattern, player)):
            print("Please enter a valid name!")
        else:
            print(f"Welcome {player}!")
            break


def show_menu():
    user()
    print(f"""
    *********************************
    It`s time to play some Blackjack!
    *********************************
    """)


def blackjack():
    pass


show_menu()

'''
Deck de 52 cartas um lista
1 jogador e um dealer
1 partida
2 cartas (de inicio pra cada)
As = 1
Cartas do dealer reveladas apenas no fim
condicoes de vitoria:
    - mais pontos que o dealer
    - ou ao atingir 21
Dealer auto (ou ganha ou estora em pontos)
Vitoria do dealer proximidade de 21 ou 21
Nao mostrar valor somente o naipe ou valor
A carta que sai do deck sai da lista
'''
