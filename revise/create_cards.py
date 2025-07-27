#!/usr/bin/env python3
import sqlite3
# here is  some code to manage flashcards using SQLite
# This code allows you to create decks, add cards, and manage flashcards.
#We will make an official flashcards app with this code after we agree on it.
DB_NAME = 'flashcards.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS deck (
                    deck_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE)''')
    c.execute('''CREATE TABLE IF NOT EXISTS card (
                    card_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    deck_id INTEGER NOT NULL,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    FOREIGN KEY (deck_id) REFERENCES deck(deck_id) ON DELETE CASCADE)''')
    conn.commit()
    conn.close()

def get_decks():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT name FROM deck")
    decks = [row[0] for row in c.fetchall()]
    conn.close()
    return decks

def create_deck(name):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO deck (name) VALUES (?)", (name,))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Deck already exists.")
    conn.close()

def get_deck_id(name):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT deck_id FROM deck WHERE name=?", (name,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

def add_card(deck_id, question, answer):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO card (deck_id, question, answer) VALUES (?, ?, ?)", (deck_id, question, answer))
    conn.commit()
    conn.close()

def main():
    init_db()
    while True:
        print("\nAvailable decks:")
        for deck in get_decks():
            print(f" - {deck}")
        deck_choice = input(">>>> Choose a deck or create a new one: ").strip()
        if deck_choice.lower() in ["cancel", "switch"]:
            break
        create_deck(deck_choice)
        deck_id = get_deck_id(deck_choice)

        while True:
            question = input(f">>>> Add new question in '{deck_choice}' deck (or type Cancel/Switch): ")
            if question.lower() in ["cancel", "switch"]:
                break
            answer = input(">>>> Provide the answer: ")
            add_card(deck_id, question, answer)
            print("—---------------------------------------------------")

if __name__ == "__main__":
    main()