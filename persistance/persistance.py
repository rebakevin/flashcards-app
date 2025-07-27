import sqlite3
class DataHandler:
    def __init__(self, db_path='flashcards.db'):
        self.db_path = db_path
        self._init_database()
    
    def _get_connection(self):
        """Get a new database connection"""
        return sqlite3.connect(self.db_path)
    
    def _init_database(self):
        """Initialize the database with tables if they don't exist"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        # Create decks table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS decks (
                deck_id INTEGER PRIMARY KEY AUTOINCREMENT,
                deck_name TEXT NOT NULL
            )
        ''')
        
        # Create cards table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cards (
                card_id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                deck_id INTEGER NOT NULL,
                FOREIGN KEY (deck_id) REFERENCES decks(deck_id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    # Handle decks
    
    def create_deck(self, name):
        """Create a new deck"""
        conn = self._get_connection()
        cursor = conn.cursor()
        try:
            decks = [deck[1] for deck in self.get_all_decks()]
            if name not in decks:
                cursor.execute(
                    "INSERT INTO decks (deck_name) VALUES (?)",
                    (name,)
                )
                deck_id = cursor.lastrowid
                conn.commit()
                print(f"Created deck '{name}' with ID: {deck_id}")
                return deck_id
            raise Exception(f"Deck '{name}' already exists")   
        except Exception as e:
            conn.rollback()
            return str(e)
        finally:
            conn.close()
    
    def get_all_decks(self):
        """Get all decks"""
        conn = self._get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT deck_id, deck_name FROM decks")
            decks = cursor.fetchall()
            return decks
        finally:
            conn.close()
    
    def get_deck(self, deck_id):
        """Get a specific deck by ID"""
        conn = self._get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT deck_id, deck_name FROM decks WHERE deck_id = ?", (deck_id,))
            deck = cursor.fetchone()
            return deck
        finally:
            conn.close()
            
    def get_deck_by_name(self, name):
        """Get a specific deck by name"""
        conn = self._get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT deck_id, deck_name FROM decks WHERE deck_name = ?", (name,))
            deck = cursor.fetchone()
            return deck
        finally:
            conn.close()
    
    def update_deck(self, deck_id, new_name):
        """Update a deck's name"""
        conn = self._get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE decks SET deck_name = ? WHERE deck_id = ?",
                (new_name, deck_id)
            )
            conn.commit()
            return cursor.rowcount > 0  # Returns True if a row was updated
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()
    
    def delete_deck(self, deck_id):
        """Delete a deck and all its cards"""
        conn = self._get_connection()
        cursor = conn.cursor()
        try:
            # Delete all cards in the deck first
            cursor.execute("DELETE FROM cards WHERE deck_id = ?", (deck_id,))
            # Then delete the deck
            cursor.execute("DELETE FROM decks WHERE deck_id = ?", (deck_id,))
            conn.commit()
            return cursor.rowcount > 0  # Returns True if a row was deleted
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()
    
    # Handle cards
    
    def create_card(self, question, answer, deck_id):
        """Create a new card in a deck"""
        conn = self._get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO cards (question, answer, deck_id) VALUES (?, ?, ?)",
                (question, answer, deck_id)
            )
            card_id = cursor.lastrowid
            conn.commit()
            return card_id
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()
    
    def get_all_cards(self, deck_id=None):
        """Get all cards, optionally filtered by deck_id"""
        conn = self._get_connection()
        cursor = conn.cursor()
        try:
            if deck_id:
                cursor.execute(
                    "SELECT card_id, question, answer, deck_id FROM cards WHERE deck_id = ?",
                    (deck_id,)
                )
            else:
                cursor.execute("SELECT card_id, question, answer, deck_id FROM cards")
            cards = cursor.fetchall()
            return cards
        finally:
            conn.close()
    
    def get_card(self, card_id):
        """Get a specific card by ID"""
        conn = self._get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "SELECT card_id, question, answer, deck_id FROM cards WHERE card_id = ?",
                (card_id,)
            )
            card = cursor.fetchone()
            return card
        finally:
            conn.close()
    
    def update_card(self, card_id, question=None, answer=None, deck_id=None):
        """Update a card's question, answer, or deck"""
        conn = self._get_connection()
        cursor = conn.cursor()
        try:
            # Build dynamic update query
            updates = []
            params = []
            
            if question is not None:
                updates.append("question = ?")
                params.append(question)
            if answer is not None:
                updates.append("answer = ?")
                params.append(answer)
            if deck_id is not None:
                updates.append("deck_id = ?")
                params.append(deck_id)
            
            if not updates:
                return False  # Nothing to update
            
            params.append(card_id)  # Add card_id for WHERE clause
            
            query = f"UPDATE cards SET {', '.join(updates)} WHERE card_id = ?"
            cursor.execute(query, params)
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()
    
    def delete_card(self, card_id):
        """Delete a card"""
        conn = self._get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM cards WHERE card_id = ?", (card_id,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()


# Initialize handler            
data_handler = DataHandler()
