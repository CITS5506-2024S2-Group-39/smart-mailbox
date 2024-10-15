import sqlite3
import os
from config import DATABASE


# Function to initialize the database
def initialize_db():
    # Remove the old database file if it exists
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
        print(f"Old {DATABASE} removed.")

    # Connect to the new database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Create events table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time TEXT,
            type TEXT,
            data TEXT
        );
    """
    )

    # Create settings table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT
        );
    """
    )

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print(f"New {DATABASE} initialized with tables 'events' and 'settings'.")


if __name__ == "__main__":
    initialize_db()
