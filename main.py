from utils.data import DataHandler
from create.creating_cards import create_card
from revise.revise_cards import revise_cards

data_handler = DataHandler()


print('Welcome to Flashcards App!')
print('The science of memory, one card at a time.')

print('Choose to create cards [C] or to revise [L]')
choice = input("Enter something: ")

match choice:
    case 'C':
       create_card()
    case 'L':
        revise_cards()
    case _:
        print('Invalid choice. Please choose between C or L')