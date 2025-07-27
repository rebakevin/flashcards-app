from persistance.persistance import DataHandler
from persistance.delete_resource import delete_resource
from create.creating_cards import creating_cards
from revise.revise_cards import revise_cards
from utils.exit import check_for_exit
from utils.draw_line import draw_line

data_handler = DataHandler()
def menu():
    """Display the main menu and get user mode"""
    print('Welcome to Flashcards App!')
    print('The science of memory, one card at a time.')
    print('-'*30)
    print()
    
    app_instructions()
    
    mode = input("Choose [C], [L] or [D]: ")
    check_for_exit(mode)
    return mode.upper()


def app_instructions():
    print('APP INSTRUCTIONS')
    draw_line()
    print()
    
    print('---- Modes ----')
    print()
    print('1. Type [C] to create cards')
    print('2. Type [L] to revise cards')
    print('3. Type [D] to delete a deck or a card')
    print('4. Type [Exit] to close the app')
    print('5. Type [Cancel] to quit the current mode')
    print('6. Type [Switch] to switch to another mode')
    print()
    print('---- When Revising ----')
    print()
    print('1. Press [R] to reveal answer')
    print('2. Press [Enter] key to continue')
    print()



def main():
    mode = menu()
    
    while True:
        match mode:
            case 'C':
                result = creating_cards()
                if result == 'cancel':
                    mode = menu()
                elif result == 'switch':
                    mode = 'L'
                    print("\nSwitched to revising mode!")
                    print('-'*30)
                else: 
                    mode = menu()
                    
            case 'L':
                result = revise_cards()
                if result == "cancel":
                    mode = menu()
                elif result == "switch":
                    mode = 'C'
                    print("\nSwitched to create mode!")
                    print('-'*30)
                else:
                    mode = menu()
            case 'D':
                delete_resource()
                mode = menu()
            case _:
                print()
                mode = input("Invalid mode. Please choose between C or L: ")
                check_for_exit(mode)
                

if __name__ == "__main__":
    main()