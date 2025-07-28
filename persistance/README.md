# Flashcards App - Persistence Module

## Overview
The persistence module handles all data storage and retrieval operations for the Flashcards App. It manages the creation, reading, updating, and deletion of flashcard decks stored in CSV files.

## Key Components
### Persistence.py
This core file provides essential functionality for:
- Creating new decks
- Saving cards to decks
- Reading cards from decks
- Managing deck files
- Handling file operations safely

## Data Structure
- Each deck is stored in a separate CSV file named `[deck_name]_deck.csv`
- CSV files contain two columns:
  - Question (first column)
  - Answer (second column)

## Features
- Atomic file operations to prevent data corruption
- Error handling for file operations
- Deck existence validation
- Safe file creation and writing
- Support for multiple decks

## Usage
The persistence module is used internally by other parts of the application:
1. When creating new cards
2. When reviewing cards
3. When switching between decks
4. When managing card data

## File Operations
- Files are stored locally in the same directory
- Each deck maintains its own file
- Files are created with proper headers
- Data is written in UTF-8 encoding
- Files are closed properly after operations

## Error Handling
The module includes robust error handling for:
- File not found errors
- Permission errors
- Invalid file formats
- Data corruption
- Duplicate deck names

## Best Practices
- Always validate deck names before operations
- Handle file operations atomically
- Use proper error handling for all operations
- Maintain consistent file naming conventions
- Regularly back up your deck files

## Security
- Files are stored locally only
- No cloud storage or external connections
- Data is stored in plain CSV format
- No encryption implemented (consider implementing for sensitive data)

## Contributing
This module is crucial for the application's data integrity. Any contributions should:
1. Maintain atomic file operations
2. Preserve data consistency
3. Add robust error handling
4. Follow existing code patterns

## License
This project is designed for educational purposes and is open source.
