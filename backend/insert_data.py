import sqlite3

DATABASE = 'mailbox.db'

# Function to insert test data into the events table
def insert_test_data():
    # Connect to the database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Insert a test event into the events table
    cursor.execute('''
        INSERT INTO events (time, type, data) VALUES (?, ?, ?)
    ''', ("2024-10-11 15:00:00", "New Mail", "{'summary': 'Test Mail Event'}"))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Test event inserted successfully.")

# Make sure the code inside this block is indented properly
if __name__ == "__main__":
    insert_test_data()
