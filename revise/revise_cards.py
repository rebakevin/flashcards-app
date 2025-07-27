from utils.persistance import DataHandler

data_handler = DataHandler()


def revise_cards():
    print('Revise a deck')
    decks = data_handler.get_all_decks()
    for deck in decks:
        print(f"{deck[0]} - {deck[1]}")
        
    deck = input('Choose deck to revise: ')
    data_handler.get_deck_by_name(deck)
    
    print(f'You selected: {deck} deck.')