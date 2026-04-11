import random
class Deck():
    """
    Class representing a deck of cards.

        Parameters:
            size (int): number of cards in the deck.

        Variables:
            card_list (list): list of the available cards in the deck.
            cards_in_play_list (list): cards in the user's hand.
            discards_list (list): discards cards in the user's hand.

        Logic:
            1. Creates a deck of cards.
            2. Shuffles the cards in the deck.
            3. Deals the cards in the deck.
            4. Gives the opportunity to discard the cards in the user's hand.

        Return:
            None
    """
    def __init__(self, size):
        #Creates the deck of cards and shuffles them.
        self.card_list = [i for i in range(size)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.card_list)
            self.card_list =self.discards_list
            self.discards_list = []
            print("Reshuffling...!!!")
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card

    def new_hand(self):
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()

    def your_hand(self, ranks, suits):
        hand = []
        #Deals the 5 cards in the user's hand.
        print("Your hand:")
        for i in range(5):
            d = self.deal()
            hand.append(d)
            r = d % 13
            s = d // 13
            print(ranks[r], 'of', suits[s])
        print()
        return hand

    def replace_hand(self, hand, ranks, suits):
        choice = input("Enter the cards you want to replace: ")
        if choice != "":
            for x in choice.split():
                pos = int(x) - 1
                if 0 <= pos < 5:
                    hand[pos] = self.deal()


        print("Your new hand: ")
        for d in hand:
            r = d % 13
            s = d // 13
            print(ranks[r], 'of', suits[s])
        print()


def main():
    """
    Main program for the game.

    Parameters:
        None

    Variables:
        ranks (list): card ranks.
        suits (list): card suits.
        my_deck (class): deck of cards.
        hands (list): list of the cards in the user's hand.

    Logic:
         1. Creates a deck of cards.
        2. Shuffles the cards in the deck.
        3. Deals the cards in the deck.
        4. Gives the opportunity to discard the cards in the user's hand.

    Return:
         None
    """
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    my_deck = Deck(52)

    hand = my_deck.your_hand(ranks, suits)
    my_deck.new_hand()

    my_deck.replace_hand(hand, ranks, suits)




if __name__ == "__main__":
    main()

