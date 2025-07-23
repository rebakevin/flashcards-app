from utils.data import DataHandler

data_handler = DataHandler()

def create_card():
    print('Use a new deck')
    deck_name = input('Deck name: ')
    
    existing_decks = [deck[1] for deck in data_handler.get_all_decks()]
    
    if(deck_name in existing_decks):
        print(f'Using {deck_name}')
        return
    else:
        data_handler.create_deck(deck_name)
        return None