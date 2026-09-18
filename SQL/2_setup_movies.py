import psycopg2

DB_CONFIG = {
    "dbname": "practice_db",
    "user": "ariel",
    "password": "12345678",
    "host": "localhost",
    "port": "5432"
}

try:
    conn = psycopg2.connect(**DB_CONFIG)
    conn.autocommit = True
    cur = conn.cursor()

    # Reset table
    cur.execute("DROP TABLE IF EXISTS movies;")
    
    # Create table
    cur.execute("""
        CREATE TABLE movies (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            director VARCHAR(100),
            release_year INTEGER,
            genre VARCHAR(50),
            rating DECIMAL(3,1),
            box_office INTEGER -- in millions
        );
    """)

    # Insert data
    movies_data = [
        ("Inception", "Christopher Nolan", 2010, "Sci-Fi", 8.8, 836),
        ("The Dark Knight", "Christopher Nolan", 2008, "Action", 9.0, 1004),
        ("Interstellar", "Christopher Nolan", 2014, "Sci-Fi", 8.6, 677),
        ("Pulp Fiction", "Quentin Tarantino", 1994, "Crime", 8.9, 213),
        ("The Matrix", "Lana Wachowski", 1999, "Sci-Fi", 8.7, 463),
        ("Forrest Gump", "Robert Zemeckis", 1994, "Drama", 8.8, 677),
        ("The Godfather", "Francis Ford Coppola", 1972, "Crime", 9.2, 245)
    ]
    
    cur.executemany("INSERT INTO movies (title, director, release_year, genre, rating, box_office) VALUES (%s, %s, %s, %s, %s, %s);", movies_data)
    print("✅ Movie database setup complete!")

except Exception as e:
    print(f"❌ Error: {e}")
finally:
    if 'cur' in locals(): cur.close()
    if 'conn' in locals(): conn.close()