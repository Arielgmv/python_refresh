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
# EXERCISE 1: INNER JOIN
# ==========================================
def get_movies_with_actors():
    """Write a query using INNER JOIN to get the movie title and the actor's name.
    Hint: You will need to join movies, movie_actors, and actors."""
    conn = get_connection()
    cur = conn.cursor()
    
    query = """
    -- YOUR SQL HERE --
    """
    
    cur.execute(query)
    print("\n--- Movies and their Actors ---")
    for row in cur.fetchall():
        print(f"{row[0]} starring {row[1]}")
        
    cur.close()
    conn.close()

# ==========================================
# EXERCISE 2: LEFT JOIN
# ==========================================
def get_all_movies_even_without_actors():
    """Write a query using LEFT JOIN to get ALL movies. 
    If a movie doesn't have an actor linked, it should still show up (with NULL for the actor)."""
    conn = get_connection()
    cur = conn.cursor()
    
    query = """
    -- YOUR SQL HERE --
    """
    
    cur.execute(query)
    print("\n--- All Movies (Left Join) ---")
    for row in cur.fetchall():
        actor = row[1] if row[1] else "No actor listed"
        print(f"{row[0]} -> {actor}")
        
    cur.close()
    conn.close()

# ==========================================
# EXERCISE 3: Pattern Matching (LIKE)
# ==========================================
def find_movies_starting_with_the():
    """Write a query to find all movies where the title starts with the word 'The'.
    Hint: Use the LIKE operator and the % wildcard."""
    conn = get_connection()
    cur = conn.cursor()
    
    query = """
    -- YOUR SQL HERE --
    """
    
    cur.execute(query)
    print("\n--- Movies starting with 'The' ---")
    for row in cur.fetchall():
        print(row[0])
        
    cur.close()
    conn.close()

# ==========================================
# EXERCISE 4: Subqueries
# ==========================================
def find_movies_by_actor_name(actor_name):
    """Write a query to find the title of the movie starring a specific actor.
    Hint: You can do this with JOINs, but try using a SUBQUERY (SELECT inside a SELECT) in the WHERE clause!"""
    conn = get_connection()
    cur = conn.cursor()
    
    query = """
    -- YOUR SQL HERE --
    """
    
    cur.execute(query, (actor_name,))
    print(f"\n--- Movies starring {actor_name} ---")
    for row in cur.fetchall():
        print(row[0])
        
    cur.close()
    conn.close()

# --- RUN THE EXERCISES ---
if __name__ == "__main__":
    get_movies_with_actors()
    get_all_movies_even_without_actors()
    find_movies_starting_with_the()
    find_movies_by_actor_name("Keanu Reeves")