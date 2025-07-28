# Flashcards App - Card Creation Module

## Overview
This module is part of the Flashcards App, a terminal-based application designed to help students learn new concepts efficiently using spaced repetition. The `creating_cards.py` script allows users to create and manage flashcard decks.

## Features
- Create new flashcard decks
- Add questions and answers to existing decks
- Organize cards into different subject decks
- Store cards in CSV files for easy management
- Support for canceling operations or switching to review mode

## Usage
1. Run the script in your terminal
2. Choose to create cards (option 'C')
3. Select an existing deck or create a new one
4. Enter questions and answers
5. Use 'Cancel' to stop creating cards
6. Use 'Switch' to switch to review mode

## File Structure
- Each deck is stored in a separate CSV file ([deck_name]_deck.csv)
- CSV files contain two columns: Question and Answer
- Files are stored locally in the same directory

## Requirements
- Python 3.x
- No external dependencies required

## Best Practices
- Keep related cards in the same deck
- Write clear, concise questions
- Provide complete, accurate answers
- Regularly review and update your cards

## Error Handling
- Invalid deck names will prompt for re-entry
- Empty questions or answers will be rejected
- Safe handling of file operations to prevent data loss

## Contributing
This module is part of a larger educational project. Contributions and improvements are welcome!

## License
This project is designed for educational purposes and is open source.