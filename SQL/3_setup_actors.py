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

    # 1. Create the actors table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS actors (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        );
    """)

    # 2. Create a junction table to link movies and actors (Many-to-Many relationship)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS movie_actors (
            movie_id INTEGER REFERENCES movies(id),
            actor_id INTEGER REFERENCES actors(id),
            PRIMARY KEY (movie_id, actor_id)
        );
    """)

    # 3. Insert some actors
    actors_data = [
        ("Keanu Reeves",),
        ("Leonardo DiCaprio",),
        ("John Travolta",),
        ("Al Pacino",)
    ]
    cur.executemany("INSERT INTO actors (name) VALUES (%s) ON CONFLICT DO NOTHING;", actors_data)

    # 4. Link actors to movies (Using the IDs from your existing movies table)
    # Note: We use subqueries here just to make the setup script robust regardless of your movie IDs!
    links = [
        ("The Matrix", "Keanu Reeves"),
        ("Inception", "Leonardo DiCaprio"),
        ("Pulp Fiction", "John Travolta"),
        ("The Godfather", "Al Pacino")
    ]
    
    for movie_title, actor_name in links:
        cur.execute("""
            INSERT INTO movie_actors (movie_id, actor_id)
            VALUES (
                (SELECT id FROM movies WHERE title = %s),
                (SELECT id FROM actors WHERE name = %s)
            ) ON CONFLICT DO NOTHING;
        """, (movie_title, actor_name))

    print("✅ Actors and relationships added successfully!")

except Exception as e:
    print(f"❌ Error: {e}")
finally:
    if 'cur' in locals(): cur.close()
    if 'conn' in locals(): conn.close()