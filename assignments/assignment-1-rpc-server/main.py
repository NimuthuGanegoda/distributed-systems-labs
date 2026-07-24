"""
main.py

Simple launcher script to start everything at once.
"""

import os
import subprocess
import sys
import time


def main():
    print("-" * 40)
    print("   BANKING SYSTEM LAUNCHER")
    print("-" * 40)
    
    # Get current folder
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Full paths to scripts
    db_script = os.path.join(base_dir, "db_server.py")
    app_script = os.path.join(base_dir, "server.py")
    client_script = os.path.join(base_dir, "client.py")
    
    # Check if files exist
    if not all(os.path.exists(f) for f in [db_script, app_script, client_script]):
        print("ERROR: Missing files!")
        sys.exit(1)

    print(f"Using Python: {sys.executable}")
    
    # 1. Start DB Server
    print("Starting DB Server...")
    try:
        # Run it in the background using python executable
        db_process = subprocess.Popen([sys.executable, db_script])
    except Exception as e:
        print(f"Failed to start DB: {e}")
        sys.exit(1)
        
    # Wait for 2 seconds to let it load before we start the next one
    time.sleep(2) 
    
    # Check if it crashed right away
    if db_process.poll() is not None:
        print("Error: DB Server failed to start.")
        sys.exit(1)

    # 2. Start Application Server
    print("Starting App Server...")
    try:
        # Run it in the background
        app_process = subprocess.Popen([sys.executable, app_script])
    except Exception as e:
        print(f"Failed to start App Server: {e}")
        # Make sure to close DB server if App server fails
        db_process.terminate()
        sys.exit(1)
        
    time.sleep(2) 

    # Check if App Server crashed
    if app_process.poll() is not None:
        print("Error: App Server failed to start.")
        db_process.terminate()
        sys.exit(1)

    # 3. Start Client
    print("Starting Client...")
    print("-" * 40)
    
    try:
        # Run the client in the foreground so the user can see it
        # subprocess.run waits until the command finishes
        subprocess.run([sys.executable, client_script])
        
    except KeyboardInterrupt:
        # Handle Control+C
        print("\nStopped.")
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        # When Client finishes (user exit), close the background servers
        print("\nClosing servers...")
        
        # Check if DB process is running, then kill it
        if 'db_process' in locals() and db_process.poll() is None:
            db_process.terminate()
            db_process.wait()
            
        # Check if App process is running, then kill it
        if 'app_process' in locals() and app_process.poll() is None:
            app_process.terminate()
            app_process.wait()
        
        print("Done.")
        print("-" * 40)

if __name__ == "__main__":
    main()
