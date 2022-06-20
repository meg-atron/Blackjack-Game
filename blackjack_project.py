
import random
import time


def player_bust():
    print(f"Player total is {player_total}.")
    time.sleep(2)
    print("Player busts. Dealer wins")


def player_stand():

    if player_total == 21 and dealer_total == 21:
        print("Dealer has 21!  It's a tie!")
    else:
        print(f"Player has {player_total}")
        dealer_turn(dealer_total)


def dealer_turn(dealer_total):
    time.sleep(2)
    print(f"Dealer hand: {dealer_hand}")
    time.sleep(2)
    if player_total == 21 and dealer_total == 21:
        print("Player and Dealer have 21.")
        time.sleep(1)
        print("It's a tie!")
    elif player_total == dealer_total:
        print(
            f"Player has {player_total} Dealer has {dealer_total}.  It's a tie!")
    elif dealer_total == 21:
        print("Dealer has 21.  Dealer wins")
    else:
        while dealer_total < 17:
            print("Dealer hits")
            dealer_hand.append(deck.pop())
            time.sleep(1.5)
            print(dealer_hand)
            time.sleep(1)
            dealer_total = hand_value(dealer_hand)
        if dealer_total > 21:
            print(
                f"Dealer busts with a total of {dealer_total}.  Player wins!")
        elif dealer_total == player_total:
            print(
                f"Player has {player_total} Dealer has {dealer_total}.  It's a tie!")
        elif dealer_total > player_total:
            print(f"Dealer has {dealer_total}.")
            time.sleep(1)
            print(f"Player has {player_total}.")
            print("Dealer wins.")
        else:
            print(
                f"Dealer has {dealer_total}. Player has {player_total}. Player wins!")


def hand_value(hand):
    total = 0
    ace_count = 0
    for card in hand:
        if card[0] == '1' and card[1] == '0':
            total += 10
        elif card[0].isnumeric():
            total += int(card[0])
        elif card[0] == 'A':
            ace_count += 1
        else:
            total += 10
    while ace_count > 0:
        if total + 11 > 21:
            total += 1
        else:
            total += 11
        ace_count -= 1
    # print(total)
    return total


deck_values = ["1", "2", "3", "4", "5", "6",
               "7", "8", "9", "10", "J", "Q", "K", "A"]
deck_suits = ["H", "D", "C", "S"]
deck = [value + suit
        for suit in deck_suits for value in deck_values]

random.shuffle(deck)
# print(deck)
answer = "y"
while answer == "y":
    if len(deck) < 10:
        print("Shuffling new deck...")
        time.sleep(5)
        random.shuffle(deck)
    dealer_hand = []
    player_hand = []

    for card in range(2):
        dealer_hand.append(deck.pop())
    for card in range(2):
        player_hand.append(deck.pop())

    dealer_total = hand_value(dealer_hand)
    player_total = hand_value(player_hand)
    # print(dealer_hand)
    print(f"Player hand: {player_hand}")
    time.sleep(2)
    while player_total <= 21:
        if player_total == 21:
            print("Player has 21.  Player stands.")
            dealer_turn(dealer_total)
            break
        print(f"Your card total is: {player_total}")
        time.sleep(1)
        choice = input("Enter 1 to hit. Enter 2 to stand: ")
        if choice == "1":
            print("Player hits")
            player_hand.append(deck.pop())
            time.sleep(1)
            print(player_hand)
            time.sleep(2)
            player_total = hand_value(player_hand)
            if player_total > 21:
                player_bust()
                break
        elif choice == "2":
            print("Player stands.")
            time.sleep(2)
            player_stand()

            break
        else:
            print("Please enter a valid choice.")
    answer = input("Do you want to play again?(y/n) ")

# Do you want to play again?
