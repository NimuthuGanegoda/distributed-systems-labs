"""
shared.py

Holds the constants and the fee calculation function used by both servers.
"""

# Server details
DB_HOST = 'localhost'
DB_PORT = 8001

APP_HOST = 'localhost'
APP_PORT = 8000

def calculate_fee(amount):
    """
    Returns the fee based on the assignment table.
    """
    # If the amount is small (<= 2000), it's free
    if amount <= 2000:
        return 0.0
    
    # If amount is between 2000 and 10000
    # Fee is 0.25%, but we cap it at max $20
    elif amount <= 10000:
        fee = amount * 0.0025
        return min(fee, 20.00)
    
    # If amount is between 10000 and 20000
    # Fee is 0.20%, max $25
    elif amount <= 20000:
        fee = amount * 0.0020
        return min(fee, 25.00)
    
    # If amount is between 20000 and 50000
    # Fee is 0.125%, max $40
    elif amount <= 50000:
        fee = amount * 0.00125
        return min(fee, 40.00)
    
    # If amount is between 50000 and 100000
    # Fee is 0.08%, max $50
    elif amount <= 100000:
        fee = amount * 0.0008
        return min(fee, 50.00)
    
    # For anything bigger than 100000
    # Fee is 0.05%, max $100
    else:
        fee = amount * 0.0005
        return min(fee, 100.00)
