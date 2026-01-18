# Simple Banking System

This is a simple distributed banking system implemented in Python using XML-RPC. It consists of a client, an application server, and a database server.

## Architecture

*   **Client (`client.py`)**: Connects to the Application Server to perform banking operations.
*   **Application Server (`server.py`)**: Handles client requests, performs logic (like fee calculation), and communicates with the Database Server.
*   **Database Server (`db_server.py`)**: Manages the SQLite database (`bank.db`) and handles data persistence.
*   **Launcher (`main.py`)**: A utility script to start all three components (Client, App Server, DB Server) for testing purposes.

## Requirements

*   Python 3.x

## How to Run

### Using the Launcher

The easiest way to run the system is using the `main.py` script:

```bash
python main.py
```

This will start the Database Server and Application Server in the background, and then launch the Client in the foreground. When you exit the Client, the servers will be shut down automatically.

### Running Components Individually

You can also run each component in a separate terminal window:

1.  **Start the Database Server:**
    ```bash
    python db_server.py
    ```

2.  **Start the Application Server:**
    ```bash
    python server.py
    ```

3.  **Start the Client:**
    ```bash
    python client.py
    ```

## Verification

To run a specialized verification script that tests the system functionality:

```bash
python verify_system.py
```
