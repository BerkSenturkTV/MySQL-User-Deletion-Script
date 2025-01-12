
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def connect_to_db():
    """Connect to the database using credentials from the .env file."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def main():
    # Prompt user for UIDs to delete
    uids_to_delete = input("Enter UIDs to delete, separated by commas: ").split(',')

    # Connect to the database
    db = connect_to_db()
    cursor = db.cursor()

    deleted_uids = []
    not_found_uids = []

    for uid in uids_to_delete:
        uid = uid.strip()
        if not uid.isdigit():
            print(f"Invalid UID entered: {uid}")
            continue

        try:
            # Check if the UID exists
            cursor.execute("SELECT uID FROM Users WHERE uID = %s", (uid,))
            result = cursor.fetchone()

            if result:
                # Delete the UID
                cursor.execute("DELETE FROM Users WHERE uID = %s", (uid,))
                db.commit()
                deleted_uids.append(uid)
                print(f"UID {uid} successfully deleted.")
            else:
                not_found_uids.append(uid)
                print(f"UID {uid} not found in the database.")
        except mysql.connector.Error as err:
            print(f"Database error: {err}")

    # Process completion report
    print("\nOperation Completed.")
    print(f"Deleted UIDs: {', '.join(deleted_uids) if deleted_uids else 'None'}")
    print(f"Not Found UIDs: {', '.join(not_found_uids) if not_found_uids else 'None'}")

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
