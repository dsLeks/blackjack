import random


class GameManager():
    def __init__(self):
        # [A (11 or 1), 2, 3, 4, 5, 6, 7, 8, 9, J, Q, K]
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.dealer_cards = []
        self.hand_sum = 0

    def setPlayerHand(self, player):
        for i in range(0, 2):
            player.player_cards.append(self.cards[random.randint(0, 12)])
            player.hand_sum += player.player_cards[i]

    def start(self, p1):
        random.shuffle(self.cards)
        for i in range(0, 2):
            self.dealer_cards.append(self.cards[random.randint(0, 12)])
            self.hand_sum += self.dealer_cards[i]
        self.setPlayerHand(p1)

    def hit(self, player):
        player.player_cards.append(self.cards[random.randint(0, 12)])
        player.hand_sum += player.player_cards[-1]
        if player.hand_sum > 21:
            return "bust"
        else:
            return "added"

    def bust(self, player):
        print("The Dealer Cards are: " + str(self.dealer_cards))
        print("Your cards are: " + str(player.player_cards))
        print("You have lost! - Bust")

    def stand(self, player):
        print("The Dealer Cards are: " + str(self.dealer_cards))
        had_to_draw = False
        while self.hand_sum <= 16:
            self.dealer_cards.append(self.cards[random.randint(0, 12)])
            self.hand_sum += self.dealer_cards[-1]
            had_to_draw = True
        if had_to_draw:
            print("The Dealer Cards after drawing now are : " +
                  str(self.dealer_cards))
        if self.hand_sum >= 21 and player.hand_sum >= 21:
            return "Tie"
        elif self.hand_sum < 21 and player.hand_sum > 21:
            return "Dealer Won"
        elif self.hand_sum > 21 and player.hand_sum < 21:
            return "Player Won"

    def quit():
        pass
