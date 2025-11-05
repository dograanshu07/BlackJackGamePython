import Card as card
import Deck as deck
import Hand as hand
import Chips as chips

playing = True
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry Please provide an integer.')
        else:
            if chips.bet > chips.total:
                print(f'Sorry You do not have enough chips| you have {chips.total} chips')
            else:
                break


def hit(deck, hand_method):
    hand_method.add(deck.deal())
    hand_method.adjust_for_ace()


def hit_or_stand(deck, hand):
    # to control an upcoming while loop
    playing = True
    while True:
        x = input('Hit or Stand? (h or s): ')
        if x[0].lower() == 'h':
            print('entering h')
            hit(deck, hand)
        elif x[0].lower() == 's':
            print('Player Stands Dealers turn')
            playing = False
        else:
            print('Sorry I did not understand it | Please enter h or s.')
            continue
        break
        return playing


def show_some(player, dealer):
    print("\n Dealer's hand")
    print('first card')
    print(dealer.cards[1])
    print("\n Player's hand")
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    print("\n Dealer's hand")
    for card in dealer.cards:
        print(card)
    print(f'Value of the dealers hand: {dealer.value}')

    print("\n Player's hand")
    for card in player.cards:
        print(card)
    print(f'Value of the players hand: {player.value}')


def player_busts(player, dealer, chips):
    print("Bust Player")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print(" Player Win")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Bust Dealer| Player Win")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print(" Dealer Win")
    chips.lose_bet()


def push(player, dealer):
    print('Dealer and Player tie| Push ')