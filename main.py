import sys
from db_connection import get_connection

def main():
    arguments = sys.argv[1:]

    # If you didn't type anything, stop here
    if not arguments:
        print("Usage: python main.py [table_name]")
        print("Example: python main.py students")
        return

    # Grab the first word typed after main.py
    target_table = arguments[0].lower()

    conn = get_connection()
    if conn is None:
        return

    cursor = conn.cursor()

    # Direct word matching check
    if target_table == "companies":
        print("Scanning Table: COMPANIES")
        cursor.execute("SELECT * FROM companies;")
        for row in cursor.fetchall(): print(row)

    elif target_table == "students":
        print("Scanning Table: STUDENTS")
        cursor.execute("SELECT * FROM students;")
        for row in cursor.fetchall(): print(row)

    elif target_table == "jobs":
        print("Scanning Table: JOBS")
        cursor.execute("SELECT * FROM jobs;")
        for row in cursor.fetchall(): print(row)

    elif target_table == "applications":
        print("Scanning Table: APPLICATIONS")
        cursor.execute("SELECT * FROM applications;")
        for row in cursor.fetchall(): print(row)

    else:
        print(f"Error: You typed '{target_table}'. This is not a valid table name.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()