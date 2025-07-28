# Flashcards App - Utility Modules

## Overview
The utils directory contains reusable utility modules that provide common functionality used across the Flashcards App. These modules handle basic operations and formatting to maintain code consistency and reduce duplication.

## Modules

### draw_line.py
Provides a simple utility function for drawing horizontal lines in the terminal for better visual separation.
- Usage: `draw_line()`
- Purpose: Creates consistent visual separators between different sections of the application

### exit.py
Handles graceful application exit conditions and cleanup.
- Usage: `exit_app()`
- Features:
  - Proper cleanup of resources
  - Consistent exit messages
  - Error handling for exit conditions

### cancel_or_switch.py
Manages user input for canceling operations or switching modes.
- Usage: `handle_cancel_or_switch()`
- Features:
  - Validates 'Cancel' and 'Switch' commands
  - Provides consistent handling across modules
  - Returns appropriate exit codes

## Usage
These utility modules are imported and used by other parts of the application:
- draw_line.py: Used for visual formatting in all modules
- exit.py: Used for proper application termination
- cancel_or_switch.py: Used in create and revise modules for mode switching

## Best Practices
- Import only the specific functions needed from each module
- Use consistent function names across modules
- Follow the same error handling patterns
- Keep utility functions small and focused

## Error Handling
Each utility module includes:
- Input validation
- Error messages
- Graceful failure conditions
- Resource cleanup

## Contributing
When adding new utility functions:
1. Keep them focused and single-purpose
2. Add proper documentation
3. Include error handling
4. Follow existing patterns
5. Add test cases

## Dependencies
- Python 3.x
- No external dependencies required
- All modules are pure Python implementations

## License
This project is designed for educational purposes and is open source.