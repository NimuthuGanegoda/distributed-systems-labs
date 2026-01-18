"""
client.py

This is the Client program.
It shows the menu and sends commands to the Server.
"""

import xmlrpc.client
import shared
import sys

def main():
    print("Connecting to Application Server...")
    
    try:
        # Connect to the App Server
        application_server = xmlrpc.client.ServerProxy(f'http://{shared.APP_HOST}:{shared.APP_PORT}')
        
        # Assume connection is good.
    except ConnectionRefusedError:
        print(f"Error: Usage server is not running at {shared.APP_HOST}:{shared.APP_PORT}")
        sys.exit(1)

    print("Connected!")
    
    current_token = None
    
    # Main loop
    while True:
        if not current_token:
            # Login Menu
            print("\n--- BANKING SYSTEM ---")
            print("1. Login")
            print("2. Exit")
            choice = input("Option: ").strip()
            
            if choice == '1':
                # Ask user for login details
                entered_username = input("Username: ")
                entered_password = input("Password: ")
                
                # Call the 'login' function on the server
                result = application_server.login(entered_username, entered_password)
                
                # Check the result
                if result and not result.startswith("ERROR"):
                    current_token = result
                    print("\nLogged In!")
                else:
                    # Show error if login failed
                    print(f"\nFailed: {result}")
            
            elif choice == '2':
                # Exit the program
                print("Bye!")
                break
            else:
                print("Bad option.")
        else:
            # Banking Menu
            print("\n--- MENU ---")
            print("1. Balance")
            print("2. Transfer")
            print("3. Logout")
            choice = input("Option: ").strip()
            
            if choice == '1':
                # Ask server for the balance
                print(application_server.check_balance(current_token))
            
            elif choice == '2':
                # Ask user for transfer details
                recipient = input("To User: ")
                amount = input("Amount: ")
                
                # Send transfer request to the server
                # We send the token so the server knows who is asking
                print(application_server.transfer(current_token, recipient, amount))
            
            elif choice == '3':
                # Logout just deletes the token locally
                current_token = None
                print("Logged out.")
            
            else:
                print("Bad option.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
