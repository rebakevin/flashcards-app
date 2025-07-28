                            Flashcard Revision Tool

## Overview
This module is part of the Flashcards App, a terminal-based application designed to help students learn new concepts efficiently using spaced repetition. The `revise_cards.py` script allows users to review and practice their flashcards using a spaced repetition system.

## Features
- Review flashcards from existing decks
- Reveal answers with the 'R' command
- Progress through cards with Enter key
- Support for canceling operations or switching to creation mode
- Graceful error handling for invalid inputs
- Sequential card review (future enhancement: spaced repetition algorithm)

## Usage
1. Run the script in your terminal
   ```bash
   python3 revise_cards.py
   ```
2. Select a deck from the list of available decks
3. For each card:
   - View the question
   - Press 'R' to reveal the answer
   - Press Enter to move to the next card
   - Type 'Cancel' to quit
   - Type 'Switch' to change to creation mode

## File Structure
- Depends on deck files ([deck_name]_deck.csv) managed by the persistence module
- Each deck file contains two columns: Question and Answer
- Files are stored locally in the same directory

## Requirements
- Python 3.x
- No external dependencies required
- Depends on the persistence module for deck management

## Best Practices
- Review cards regularly (daily recommended)
- Use spaced repetition for optimal learning
- Focus on understanding each concept before moving to the next card
- Keep track of difficult cards for additional practice

## Error Handling
- Invalid deck names will prompt for re-entry
- Invalid commands will display help message
- Missing deck files will be handled gracefully
- Safe handling of file operations to prevent data loss

## Contributing
This module is part of a larger educational project. Contributions and improvements are welcome!

## License
This project is designed for educational purposes and is open source.
