import sys

def exit_app():
    """
    Gracefully exit the flashcards application
    """
    print()
    print("Thank you for using Flashcards App!")
    print("Keep learning, one card at a time. 📚")
    print("-" * 30)
    sys.exit(0)

def check_for_exit(user_input):
    """
    Check if user wants to exit and handle it
    Returns True if user wants to exit, False otherwise
    """
    if user_input.lower() in ['exit', 'quit', 'q']:
        exit_app()
        return True
    return False