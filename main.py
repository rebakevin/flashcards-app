from utils.persistance import DataHandler
from create.creating_cards import creating_cards
from revise.revise_cards import revise_cards
from utils.exit import check_for_exit

data_handler = DataHandler()


print('Welcome to Flashcards App!')
print('The science of memory, one card at a time.')
print('-'*30)
print()

print('Choose to create cards [C] or to revise [L]')

choice = input("Enter something: ")
check_for_exit(choice)


while True:
    match choice:
        case 'C':
            creating_cards()
        case 'L':
            revise_cards()
        case 'Exit':
            print('Close the app.')
            break
        case _:
            print()
            choice = input("Invalid choice. Please choose between C or L: ")
            check_for_exit(choice)
            
