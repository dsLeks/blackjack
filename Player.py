class Player():
    def __init__(self):
        self.player_cards = []
        self.hand_sum = 0
        self.bank_amount = 1000
        self.current_bet = 0

    def is_bet_possible(self):
        if self.bank_amount >= self.current_bet:
            return True
        else:
            return False
