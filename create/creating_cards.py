#!/usr/bin/env python3

from utils.exit import check_for_exit
from utils.persistance import data_handler
from utils.draw_line import draw_line

def creating_cards():
    # This while loop will continously prompt the user to create a new deck or use an existing one.
    while True:
        print("\nAvailable decks:")
        for deck in data_handler.get_all_decks():
            print(f"{deck[0]} - {deck[1]}")
            
        deck_choice = input("Choose a deck or create a new one: ").strip()
        check_for_exit(deck_choice)
        
        if deck_choice.lower() in ["cancel", "switch"]:
            return
        
        data_handler.create_deck(deck_choice)
        deck_id = data_handler.get_deck_by_name(deck_choice)[0]

        # This while loop will help the user to keep creating as many cards as they want
        while True:
            print()
            question = input(f"Add new question in '{deck_choice}': ")
            check_for_exit(question)
            
            if question.lower() in ["cancel", "switch"]:
                break
            
            answer = input("Provide the answer: ")
            check_for_exit(answer)
            
            data_handler.create_card(question, answer, deck_id)
            draw_line()

if __name__ == "__main__":
    creating_cards()
