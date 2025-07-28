# Flashcards App

- [Canva slides presentations](https://www.canva.com/design/DAGuZczWVRc/ZMxGSdx6RhIzyRGwfOZV5A/view?utm_content=DAGuZczWVRc&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hfbe1031387)
- [Google docs planning](https://docs.google.com/document/d/11sZXK0he8QLltlNNAk2IMiegufP-iLNrABTJahO3L6E/edit?usp=sharing)
- [User flow diagram](https://www.figma.com/board/tKakUKhqTP3u4VEMns2s0C/Python-Assignment?node-id=0-1&p=f&t=8CTAsTA3qiDRxMDf-0) 

## Overview
A terminal-based flashcard application that helps students learn new concepts efficiently using spaced repetition. The app enables users to create and review flashcards for effective long-term memory retention.

## Features
- Create and manage flashcard decks
- Review cards with spaced repetition
- Organize cards by subject
- Switch between creation and review modes
- Local data storage in CSV format

## How to Run
1. Install Python 3.x
2. Navigate to the app directory
3. Choose your mode:
   ```bash
   # Run the app by
   python3 main.py
   ```
4. Follow the on-screen instructions to navigate the app
5. You can run `generate_dummy_data.py` to generate starter cards if you don't want to start from scratch.
## Tools Used
- Python 3.x
- Terminal interface
- CSV files for data storage
- Pure Python implementation

## Project Structure
- `create/`: Card creation module
- `revise/`: Card review module
- `persistance/`: Data storage module
- `utils/`: Utility functions

## Getting Started
1. Create new flashcards using the creation module
2. Review cards using the revision module
3. Use 'Cancel' or 'Switch' to navigate between modes

## License
This project is designed for educational purposes and is open source.
