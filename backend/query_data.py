import sqlite3

DATABASE = 'mailbox.db'

# Function to query all events from the database
def query_events():
    # Connect to the database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Query all events
    cursor.execute('SELECT * FROM events')
    events = cursor.fetchall()

    # Print the result
    for event in events:
        print(event)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    query_events()
