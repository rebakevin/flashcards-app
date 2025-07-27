#!/usr/bin/env python3
from persistance.persistance import data_handler
from utils.draw_line import draw_line
from utils.exit import check_for_exit
from utils.cancel_or_switch import cancel_or_switch

def revise_cards():
    """Main function for revising cards using DataHandler"""
    
    print('Revise a deck')
    decks = data_handler.get_all_decks()
    for deck in decks:
        print(f"{deck[0]} - {deck[1]}")
        
    deck = input('Choose deck to revise: ')
    selected_deck = data_handler.get_deck_by_name(deck)
    if(deck in ['cancel', 'switch']):
        return cancel_or_switch(deck)
    
    if selected_deck not in decks:
        print()
        print("No decks available. Please choose between the decks above or create a new one!")
    else: 
        print(f"\nStarting revision for '{selected_deck[1]}' deck...")
        print()
        print("Press 'R' to reveal answer, Enter to continue, 'Cancel' to quit, 'Switch' to change mode")
        
        while True:
            cards = data_handler.get_all_cards(selected_deck[0])
            result = revising_algorithm(cards)
            return cancel_or_switch(result)

def revising_algorithm(cards):
    number_of_cards_revised = 0
    
    # Go through each card
    for _, question, answer, _ in cards:
        
        print(f"Question {number_of_cards_revised + 1}: {question}")
        
        while True:
            # Keep track of the cards revised in order to know when all the cards have been finished in the deck
            number_of_cards_revised += 1
            if number_of_cards_revised == len(cards):
                print(f"You've completed all {number_of_cards_revised} cards in this deck!")
                draw_line()
                check_for_exit('exit')
                
            user_input = input("").strip()
            check_for_exit(user_input)
            
            if user_input.lower() in ["cancel", "switch"]:
                return cancel_or_switch(user_input)
            
            elif user_input.lower() == "r":
                print(f"Answer: {answer}")
                draw_line()
                break
            # Enter key pressed
            elif user_input == "":  
                draw_line()
                break
            else:
                print("Invalid input. Press 'R' to reveal answer, Enter to continue, 'Cancel' to quit, 'Switch' to change mode")
