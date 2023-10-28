import GameManager
import Player

print("Welcome to BlackJack!")
gm = GameManager.GameManager()
player = Player.Player()
bet = input(
    "Place your bet to start the game. Please bet below $1000. Your Bet: $")
player.current_bet = int(bet)

if player.is_bet_possible():
    player.bank_amount -= player.current_bet
    gm.start(player)
    print("Dealer's first card: " + str(gm.dealer_cards[0]))
    print("Your cards: " + str(player.player_cards))
    playing = True
    while playing:
        choice = input("Would you like to 'hit' or 'stand'? ")
        if choice == "hit":
            hit_response = gm.hit(player)
            print("Dealer's cards: " + str(gm.dealer_cards[0]))
            print("Your cards: " + str(player.player_cards))
            if hit_response == "added":
                pass
            else:
                gm.bust(player)
                playing = False
        else:
            stand_response = gm.stand(player)
            if stand_response == "Tie":
                print("Tie!")
            elif stand_response == "Dealer Won":
                print("Dealer Won!")
            else:
                print("You Won!")
            playing = False
else:
    print("You do not have enough money to place this bet. Please try again.")
    quit()
