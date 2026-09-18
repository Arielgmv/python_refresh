import psycopg2

# 1. Database connection details
DB_CONFIG = {
    "dbname": "practice_db",
    "user": "ariel",
    "password": "12345678",
    "host": "localhost",
    "port": "5432"
}

# Helper function to print our table nicely
def print_books(cur):
    cur.execute("SELECT * FROM books ORDER BY id;")
    records = cur.fetchall() # Fetch all the rows returned by the query
    print(f"{'ID':<5} | {'Title':<25} | {'Author':<25} | {'Year'}")
    print("-" * 65)
    for row in records:
        #row is a tuple: (id, title, author, year)
        print(f"{row[0]:<5} | {row[1]:<25} | {row[2]:<25} | {row[3]}")
    print()

try:
    # Connect to the database
    conn = psycopg2.connect(**DB_CONFIG)
    # autocommit = True means we don't have to type conn.commit() after every single command
    conn.autocommit = True
    # Create a cursor object to execute SQL commands
    cur = conn.cursor()
    print("✅ Connected to PostgreSQL!\n")

    # --- STEP 1: CREATE A TABLE ---
    print("--- 1. CREATING TABLE ---")
    # We drop the table first so you can run this script multiple times cleanly!
    cur.execute("DROP TABLE IF EXISTS books;")

    create_table_query = """
    CREATE TABLE books (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        author VARCHAR(100) NOT NULL,
        year INTEGER
    );
    """
    cur.execute(create_table_query)    
    print("✅ Table 'books' created.\n")

    # --- STEP 2: INSERT DATA ---
    print("--- 2. INSERTING DATA ---")
    # We use %s as placeholders to prevent SQL injection (Best practice!)
    insert_query = """
    INSERT INTO books (title, author, year)
    VALUES (%s, %s, %s);
    """
    # A list of tuples containing the data we want to insert
    books_data = [
        ("The hobbit", "J.R.R. Tolkien", 1937),
        ("1984", "George Orwell", 1949),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    ]
    # executemany is used to insert multiple rows at once
    cur.executemany(insert_query, books_data)
    print(f"✅ Inserted {cur.rowcount} rows.\n")

    # --- STEP 3: READ DATA ---
    print("--- 3. READING DATA ---")
    print_books(cur)

    # --- STEP 4: UPDATE ---
    print("--- 4. UPDATING DATA ---")
    print("Updating '1984' year to 1950...")
    update_query = "UPDATE books SET year = %s WHERE title = %s;"
    cur.execute(update_query, (1950, "1984"))
    print(f"✅ Updated {cur.rowcount} row(s).\n")
    
    print("Current state after UPDATE:")
    print_books(cur)

    # --- STEP 5: DELETE ---
    print("--- 5. DELETING DATA ---")
    print("Deleting 'The Great Gatsby'...")
    delete_query = "DELETE FROM books WHERE title = %s;"
    cur.execute(delete_query, ("The Great Gatsby",)) # Note the comma for single-item tuples!
    print(f"✅ Deleted {cur.rowcount} row(s).\n")

    # --- STEP 6: READ ---
    print("--- 6. FINAL STATE ---")
    print_books(cur)
    print(" CRUD operations complete!")

except Exception as e:
    print(f"❌ An error occurred: {e}")

finally:
    # Always close the cursor and connection when done
    if 'cur' in locals() and cur:
        cur.close()
    if 'conn' in locals() and conn:
        conn.close()
        print("🔌 Database connection closed.")