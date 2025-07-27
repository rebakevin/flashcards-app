import sys
from utils.draw_line import draw_line

def exit_app():
    """
    Gracefully exit the flashcards application
    """
    print()
    print("Thank you for using Flashcards App!")
    print("Good session. See you next time, memory master. 💪!!!")
    draw_line()
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