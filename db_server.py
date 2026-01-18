"""
db_server.py

This is the Database Server. It handles all the SQLite database operations.
It listens for requests from the main Server.
"""

import sqlite3
import hashlib
from xmlrpc.server import SimpleXMLRPCServer
import shared
import os

DB_FILE = "bank.db"

def init_db():
    """
    Makes sure the database file and tables exist.
    Also adds some test users if the DB is empty.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Table for user info
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        balance REAL NOT NULL
    )
    ''')
    
    # Table for transaction history
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT,
        recipient TEXT,
        amount REAL,
        fee REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Add dummy data if needed
    cursor.execute("SELECT count(*) FROM users")
    # If the count is 0, it means the table is empty
    if cursor.fetchone()[0] == 0:
        print("Adding mock users...")
        # Create user A
        create_user(cursor, "userA", "passwordA", 5000.0)
        # Create user B
        create_user(cursor, "userB", "passwordB", 1000.0)
        # Create user C
        create_user(cursor, "userC", "passwordC", 20000.0)
        
        # Save the changes to the database file
        conn.commit()
    
    # Close the connection
    conn.close()

def create_user(cursor, username, password, balance):
    # Saves a new user with a hashed password
    # strict security practice: never store plain text passwords
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    # Insert the new row into the users table
    cursor.execute("INSERT INTO users (username, password, balance) VALUES (?, ?, ?)", 
                   (username, password_hash, balance))

class DBMethods:
    """
    Functions that the Server can call remotely.
    """
    
    def login(self, username, password):
        # Check if the username key and password hash match
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        cursor.execute("SELECT username FROM users WHERE username=? AND password=?", (username, password_hash))
        user_record = cursor.fetchone()
        conn.close()
        
        return user_record is not None

    def get_balance(self, username):
        """
        Retrieves the current balance for a specific user.
        Returns the balance as a float, or None if user doesn't exist.
        """
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM users WHERE username=?", (username,))
        balance_record = cursor.fetchone()
        conn.close()
        return balance_record[0] if balance_record else None

    def process_transfer(self, sender, recipient, amount, fee):
        """
        Handles the money transfer.
        It uses a transaction to make sure we don't lose money if something fails.
        """
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        try:
            # 1. Get sender's current balance
            # We look for the user with the given username
            cursor.execute("SELECT balance FROM users WHERE username=?", (sender,))
            sender_balance_record = cursor.fetchone()
            
            # If we didn't find the user
            if not sender_balance_record:
                return False, "Sender not found"
            
            # Extract the actual balance number from the record
            current_balance = sender_balance_record[0]
            
            # Calculate how much needs to be deducted
            total_deduction = amount + fee
            
            # Check if they have enough money
            if current_balance < total_deduction:
                return False, "Insufficient funds"
            
            # 2. Check if recipient exists logic
            cursor.execute("SELECT 1 FROM users WHERE username=?", (recipient,))
            if not cursor.fetchone():
                return False, "Recipient not found"
            
            # 3. Update both balances
            # Take money from sender
            cursor.execute("UPDATE users SET balance = balance - ? WHERE username=?", (total_deduction, sender))
            # Give money to recipient (without the fee)
            cursor.execute("UPDATE users SET balance = balance + ? WHERE username=?", (amount, recipient))
            
            # 4. Save record of transfer in the transactions table
            cursor.execute("INSERT INTO transactions (sender, recipient, amount, fee) VALUES (?, ?, ?, ?)",
                           (sender, recipient, amount, fee))
            
            # If everything worked, commit the transaction
            conn.commit()
            return True, "Transfer successful"
            
        except Exception as e:
            # Undo changes if any error happened inside the try block
            conn.rollback()
            return False, str(e)
        finally:
            # Always close the connection
            conn.close()

if __name__ == "__main__":
    init_db()
    
    server = SimpleXMLRPCServer((shared.DB_HOST, shared.DB_PORT), allow_none=True)
    
    # Expose functions
    server.register_instance(DBMethods())
    
    # Allow .listMethods() etc.
    server.register_introspection_functions()
    
    print(f"Database Server running on port {shared.DB_PORT}...")
    server.serve_forever()
