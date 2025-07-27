from persistance.persistance import data_handler
from utils.exit import check_for_exit

def delete_resource():
    choice = input("Choose [Deck] or [Card]: ").strip().lower()
    check_for_exit(choice)
    
    if choice in ["cancel", "switch"]:
        return choice
    
    if choice == 'deck':
        return delete_deck()
    elif choice == 'card':
        return delete_card()
    else:
        print("Invalid choice. Please choose 'Deck' or 'Card'.")
        return delete_resource()

def delete_deck():
    """Delete deck by name"""
    deck_name = input("Enter deck name to delete: ").strip()
    check_for_exit(deck_name)
    
    if deck_name.lower() in ["cancel", "switch"]:
        return deck_name.lower()
    
    deck_info = data_handler.get_deck_by_name(deck_name)
    if deck_info:
        data_handler.delete_deck(deck_info[0])
        print(f"✅ Deck '{deck_name}' deleted successfully!")
    else:
        print(f"❌ Deck '{deck_name}' not found.")
    
    input("Press Enter to continue.")
    return "completed"

def delete_card():
    """Delete card by ID"""
    try:
        card_id = input("Enter card ID to delete: ").strip()
        check_for_exit(card_id)
        
        if card_id.lower() in ["cancel", "switch"]:
            return card_id.lower()
        
        card_id = int(card_id)
        data_handler.delete_card(card_id)
        print(f"✅ Card with ID {card_id} deleted successfully!")
        
    except ValueError:
        print("❌ Invalid card ID. Please enter a number.")
    except Exception as e:
        print(f"❌ Error deleting card: {e}")
    
    input("Press Enter to continue...")
    return "completed"