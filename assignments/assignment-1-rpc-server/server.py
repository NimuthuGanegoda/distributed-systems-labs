"""
server.py

This is the main Application Server.
It sits between the Client and the Database.
It handles logging in and checking fees before talking to the DB.
"""

import uuid
import xmlrpc.client
from xmlrpc.server import SimpleXMLRPCServer

import shared

# Connect to the Database Server
print(f"Connecting to Database Server at http://{shared.DB_HOST}:{shared.DB_PORT}...")
database_server = xmlrpc.client.ServerProxy(f'http://{shared.DB_HOST}:{shared.DB_PORT}')

# Dictionary to keep active users: token -> username
active_sessions = {}

class ServerMethods:
    """
    Functions available to the Client.
    """

    def login(self, username, password):
        """
        Checks login with DB and returns a token if successful.
        """
        try:
            # Ask the Database server if the login is correct
            if database_server.login(username, password):
                # If yes, create a random token for this session
                token = str(uuid.uuid4())
                # Save the token so we know who this user is later
                active_sessions[token] = username
                print(f"User '{username}' logged in.")
                return token
            else:
                # Login failed
                return None
        except ConnectionRefusedError:
            # If the database server is offline
            return "ERROR: DB Server not reachable."

    def check_balance(self, token):
        # Make sure user is logged in
        if token not in active_sessions:
            return "ERROR: Please login again."
        
        username = active_sessions[token]
        try:
            # Get balance from DB
            balance = database_server.get_balance(username)
            if balance is not None:
                return f"Balance for {username}: ${balance:.2f}"
            else:
                return "ERROR: User not found."
        except ConnectionRefusedError:
            return "ERROR: DB Server not reachable."

    def transfer(self, token, recipient, amount):
        """
        Sends money. Calculates fee first.
        """
        # 1. Check if the user is logged in using the token
        if token not in active_sessions:
            return "ERROR: Invalid or expired token"
        
        # Get the username who is sending money
        sender = active_sessions[token]
        
        # 2. Check input validity
        try:
            # Convert amount to a number
            amount = float(amount)
        except ValueError:
            return "ERROR: Bad amount"
            
        # Can't send negative money
        if amount <= 0:
            return "ERROR: Amount must be positive"

        # Can't send money to yourself
        if sender == recipient:
            return "ERROR: You can't pay yourself."

        # 3. Calculate Fee using the shared function
        fee = shared.calculate_fee(amount)
        
        try:
            # 4. Tell the DB to do the actual transfer
            success, message = database_server.process_transfer(sender, recipient, amount, fee)
            
            if success:
                return f"SUCCESS: Sent ${amount:.2f} to {recipient} (Fee: ${fee:.2f})."
            else:
                return f"FAILURE: {message}"
        except ConnectionRefusedError:
            return "ERROR: DB Server not reachable."

if __name__ == "__main__":
    server = SimpleXMLRPCServer((shared.APP_HOST, shared.APP_PORT), allow_none=True)
    server.register_instance(ServerMethods())
    server.register_introspection_functions()
    
    print(f"Application Server running on port {shared.APP_PORT}...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping...")
