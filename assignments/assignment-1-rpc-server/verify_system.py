import xmlrpc.client
import shared
import time
import sys

def run_verification():
    print("Beginning Verification...")
    
    # Wait a moment for servers to fully start (if running in parallel script context)
    time.sleep(2) 
    
    try:
        server = xmlrpc.client.ServerProxy(f'http://{shared.APP_HOST}:{shared.APP_PORT}')
        
        # 1. Login userA
        print("1. Logging in userA...")
        token_a = server.login("userA", "passwordA")
        if not token_a or "ERROR" in token_a:
            print(f"FAILED: Login userA. Result: {token_a}")
            return
        print(f"SUCCESS: Logged in userA. Token: {token_a}")

        # 2. Check Balance userA
        print("2. Checking balance userA...")
        bal_a = server.check_balance(token_a)
        print(f"Balance: {bal_a}")
        if "5000.00" not in bal_a:
             print("FAILED: Expected balance 5000.00")
        
        # 3. Transfer from A to B
        print("3. Transferring 1000 from A to B...")
        transfer_res = server.transfer(token_a, "userB", 1000.0)
        print(f"Transfer Result: {transfer_res}")

        # 4. Login userB to verify receipt
        print("4. Logging in userB...")
        token_b = server.login("userB", "passwordB")
        bal_b = server.check_balance(token_b)
        print(f"Balance userB: {bal_b}")
        
        # 5. Verify balances
        # Fee for 1000 is 0. 
        # Wait, check shared.py:
        # Amount <= 2000 is 0% fee.
        # So A: 5000 - 1000 = 4000.
        # B: 1000 + 1000 = 2000.
        
        bal_a_new = server.check_balance(token_a)
        print(f"Final Balance A: {bal_a_new}")
        
        if "4000.00" in bal_a_new and "2000.00" in bal_b:
            print("\n*** VERIFICATION SUCCESSFUL ***")
        else:
            print("\n*** VERIFICATION FAILED - Balances incorrect ***")

    except Exception as e:
        print(f"VERIFICATION FAILED WITH EXCEPTION: {e}")

if __name__ == "__main__":
    run_verification()
