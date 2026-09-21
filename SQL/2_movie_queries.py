import psycopg2

DB_CONFIG = {
    "dbname": "practice_db",
    "user": "ariel",
    "password": "12345678",
    "host": "localhost",
    "port": "5432"
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

# ==========================================
# EXERCISE 1: Basic Filtering
# ==========================================
def find_movies_by_genre(genre):
    """Write a query to find all movies where the genre matches the input."""
    conn = get_connection()
    cur = conn.cursor()
    
    query = """
    SELECT * FROM movies
    WHERE genre = %s;
    """
    
    cur.execute(query, (genre,))
    print(f"\n--- Movies in {genre} ---")
    for row in cur.fetchall():
        print(row) # Just print the tuple for now
    
    cur.close()
    conn.close()

# ==========================================
# EXERCISE 2: Sorting and Limiting
# ==========================================
def get_top_earning_movies(limit):
    """Write a query to get the top 'limit' movies by box_office, highest first."""
    conn = get_connection()
    cur = conn.cursor()
    
    query = """
    SELECT * FROM movies
    ORDER BY box_office DESC
    LIMIT %s;
    """
    
    cur.execute(query, (limit,))
    print(f"\n--- Top {limit} Earning Movies ---")
    for row in cur.fetchall():
        print(f"{row[1]} made ${row[5]} million")
        
    cur.close()
    conn.close()

# ==========================================
# EXERCISE 3: Aggregation (COUNT / AVG)
# ==========================================
def get_average_rating_by_director():
    """Write a query to find the average rating for each director. 
    Hint: You will need GROUP BY and AVG()"""
    conn = get_connection()
    cur = conn.cursor()
    
    query = """
    SELECT director, AVG(rating) as average
    FROM movies
    GROUP BY director;
    """
    
    cur.execute(query)
    print("\n--- Average Rating by Director ---")
    for row in cur.fetchall():
        print(f"{row[0]}: {row[1]}")
        
    cur.close()
    conn.close()

# ==========================================
# EXERCISE 4: Updating Data
# ==========================================
def boost_nolan_ratings():
    """Write a query to increase the rating by 0.5 for all movies directed by 'Christopher Nolan'."""
    conn = get_connection()
    # Note: We need autocommit=False here to use commit() manually
    cur = conn.cursor()
    
    query = """
    -- YOUR SQL HERE --
    """
    
    cur.execute(query, ("Christopher Nolan",))
    conn.commit() # Don't forget to save!
    print(f"\n✅ Updated {cur.rowcount} Nolan movies.")
    
    cur.close()
    conn.close()

# ==========================================
# EXERCISE 5: Deleting Data
# ==========================================
def delete_old_movies(year):
    """Write a query to delete all movies released before the given year."""
    conn = get_connection()
    cur = conn.cursor()
    
    query = """
    -- YOUR SQL HERE --
    """
    
    cur.execute(query, (year,))
    conn.commit()
    print(f"\n🗑️ Deleted {cur.rowcount} movies older than {year}.")
    
    cur.close()
    conn.close()

# --- RUN THE EXERCISES ---
if __name__ == "__main__":
    find_movies_by_genre("Sci-Fi")
    get_top_earning_movies(3)
    get_average_rating_by_director()
    boost_nolan_ratings()
    delete_old_movies(2000)