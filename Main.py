import Card as card
import Deck as Deck
import Hand as hand
import Chips as chips
import Common as Common





class Main:
    def __init__(self):
        pass



    playing = True
    while True:
        print('Welcome to BlackJack Game')
        #create and shuffle the deck and give two cards to each
        deck = Deck.Deck()
        deck.shuffle()
        player_hand = hand.Hand()
        player_hand.add(deck.deal())
        player_hand.add(deck.deal())

        dealer_hand = hand.Hand()
        dealer_hand.add(deck.deal())
        dealer_hand.add(deck.deal())

        #Setup players chips
        player_chips = chips.Chips()
        #take bet for us
        Common.take_bet(player_chips)

        #Show card
        Common.show_some(player_hand, dealer_hand)

        while playing:
            #prompt the player to hit or stand
            playing = Common.hit_or_stand(deck, player_hand)

            #show cards
            Common.show_some(player_hand, dealer_hand)

            #if player hand exceeds 21 we are going to run player_bust and break the loop
            if player_hand.value >21:
                Common.player_busts(player_hand, dealer_hand, player_chips)
                break

            #if the player has not busted play dealers hand till its 17
        if player_hand.value <=21:
            while dealer_hand.value < 17:
                Common.hit(deck, dealer_hand)

            Common.show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                Common.dealer_busts(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value > player_hand.value:
                Common.dealer_wins(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value < player_hand.value:
                Common.player_wins(player_hand, dealer_hand, player_chips)

            else:
                Common.push(player_hand, dealer_hand)

            print(f'player total chips are : {player_chips.total}')
            new_game = input('Do you want to play another hand? (y/n): ')
            if new_game.lower() == 'y':
                playing = True
                continue
            else:
                print('Thank you for playing')
                break









