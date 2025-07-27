from utils.persistance import DataHandler
#!/usr/bin/env python3
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.persistance import DataHandler

# Initialize data handler
data_handler = DataHandler()

def revise_cards():
    print('Revise a deck')
    decks = data_handler.get_all_decks()
    for deck in decks:
        print(f"{deck[0]} - {deck[1]}")
        
    deck = input('Choose deck to revise: ')
    data_handler.get_deck_by_name(deck)
    """Main function for revising cards using DataHandler"""
    
    # Get all decks using method
    decks = data_handler.get_all_decks()
    
    if not decks:
        print(">>>> No decks available. Please create some cards first!")
        return "switch"
    
    print("\n>>>> Choose a deck of cards to revise:")
    for deck in decks:
        print(f">>>> {deck[1]}") 
    
    # Get user's deck choice
    while True:
        deck_choice = input(">>>> Choose deck to revise: ").strip()
        
        # Handle special commands
        if deck_choice.lower() == "cancel":
            return "cancel"
        elif deck_choice.lower() == "switch":
            return "switch"
        
        #  get the deck by name
        selected_deck = data_handler.get_deck_by_name(deck_choice)
        
        if selected_deck:
            print(f'>>>> You selected: {deck_choice} deck.')
            break
        else:
            print(f">>>> Deck '{deck_choice}' doesn't exist. Please choose from the available decks:")
            for deck in decks:
                print(f">>>> {deck[1]}")
    
    # Get all cards from the selected deck
    try:
        cards = data_handler.get_cards_from_deck(selected_deck[0])  # selected_deck[0] should be deck_id
    except AttributeError:
        # Temporary direct database access
        import sqlite3
        conn = sqlite3.connect('flashcards.db')
        c = conn.cursor()
        c.execute("SELECT card_id, deck_id, question, answer FROM card WHERE deck_id=?", (selected_deck[0],))
        cards = c.fetchall()
        conn.close()
    
    if not cards:
        print(f">>>> No cards found in '{deck_choice}' deck!")
        return "continue"
    
    print(f"\n>>>> Starting revision for '{deck_choice}' deck...")
    print(">>>> Press 'R' to reveal answer, Enter to continue, 'Cancel' to quit, 'Switch' to change mode")
    print(">>>>")
    
    # Go through each card
    for i, card in enumerate(cards, 1):
        question = card[2] 
        answer = card[3]
        
        print(f">>>> Question {i}: {question}")
        
        while True:
            user_input = input(">>>> ").strip()
            
            if user_input.lower() == "cancel":
                return "cancel"
            elif user_input.lower() == "switch":
                return "switch"
            elif user_input.lower() == "r":
                print(f">>>> Answer: {answer}")
                print(">>>> —---------------------------------------------------")
                break
            elif user_input == "":  # Enter key pressed
                print(">>>> —---------------------------------------------------")
                break
            else:
                print(">>>> Invalid input. Press 'R' to reveal answer, Enter to continue, 'Cancel' to quit, 'Switch' to change mode")
    
    print(f">>>> You've completed all {len(cards)} cards in '{deck_choice}' deck!")
    return "continue"

def main():
    """Main function to test the revising functionality"""
    print(">>>> Flashcards Revision Mode")
    
    while True:
        result = revise_cards()
        
        if result == "cancel":
            print(">>>> Good session. See you next time, memory master. 💪!!!")
            break
        elif result == "switch":
            print(">>>> Switching to create mode... ")
            break
        elif result == "continue":
            continue_choice = input(">>>> Would you like to revise another deck? (y/n): ").strip().lower()
            if continue_choice != 'y':
                print(">>>> Good session. See you next time, memory master. 💪!!!")
                break

if __name__ == "__main__":
    main()
