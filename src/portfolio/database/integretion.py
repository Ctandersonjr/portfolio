import psycopg

def get_connection() -> psycopg.Connection:
    return psycopg.connect(
        "postgresql://postgres:Anderson2345@localhost:5432/postgres"
    )
conn = get_connection()

with conn.cursor() as cur:
        cur.execute("""
        ALTER TABLE test DROP COLUMN IF EXISTS created_at, DROP COLUMN IF EXISTS updated_at;
        DROP TABLE IF EXISTS test;
        CREATE TABLE IF NOT EXISTS test (
            id serial PRIMARY KEY,
            username VARCHAR (50) NOT NULL,
            email VARCHAR (255)  NOT NULL UNIQUE,
            password TEXT NOT NULL,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP);
            """)

        
        cur.execute(
        """
        INSERT INTO test (username, email, password)
        VALUES (%s, %s, %s)
        RETURNING * 
        """, ("Anderson", "anderson@gmail.com", "Anderson2345"))


        print(cur.fetchone())

        cur.executemany(
            """
            INSERT INTO test (username, email, password)
            VALUES (%s, %s, %s)
            """,
            [
                ("user1", "user1@gmail.com", "Password1"),
                ("user2", "user2@gmail.com", "Password2"),
                ("user3", "user3@gmail.com", "Password3"),
            ]
        )
        cur.execute("SELECT id, username FROM test order by id")
        for record in cur:
            print(record)

        # Make the changes to the database persistent
        conn.commit()
        conn.close()