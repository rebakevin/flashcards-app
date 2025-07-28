                            Flashcard Revision Tool
This Python application is part of a collaborative flashcard system, focusing on revising flashcards interactively. 
                            
       Features
-  Deck Selection: Choose from a list of available decks provided by the data handling module.
- Interactive Revision: View questions one by one, reveal answers with 'R', continue with Enter, or cancel/switch modes.
- Persistent Data: Uses a DataHandler (from persistance.persistance) to access decks and cards.
- User-Friendly Commands: Supports 'Cancel' to quit, 'Switch' to change modes, and 'R' to reveal answers.
                       
      Prerequisites
Python 3.x installed
Custom modules (included in the project):
persistance/persistance.py (handles data storage and retrieval, developed by team members)
utils/draw_line.py (formats output with lines)
utils/exit.py (handles exit conditions)
utils/cancel_or_switch.py (manages mode switching)

      Installation

Ensure Python 3.x is installed on your system.
Clone or download the project folder containing:/project
├── revise_cards.py
├── persistance/
│   └── persistance.py
└── utils/
    ├── draw_line.py
    ├── exit.py
    └── cancel_or_switch.py




     How to run

Run the script:python3 revise/revise_cards.py


Select a deck by typing its name from the list displayed (populated by the data handling module).
For each card:
View the question.
Press R to reveal the answer.
Press Enter to move to the next card.
Type Cancel to quit or Switch to change modes.

     Notes

Invalid inputs prompt a reminder of valid commands.
The application exits gracefully when all cards are revised or upon user command.
This script depends on the data handling module (persistance.persistance) for accessing decks and cards.


