import psycopg


with psycopg.connect(
    "postgresql://postgres:Anderson2345@localhost:5432/postgres"
) as conn:

    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS test (
        id serial PRIMARY KEY,
        num integer,
        data text
    )
    """)

        
        cur.execute(
            "INSERT INTO test (num, data) VALUES (%s, %s)",
            (100, "abc'def"))
        cur.execute("SELECT * FROM test")
        print(cur.fetchone())

        cur.executemany(
            "INSERT INTO test (num) values (%s)",
            [(33,), (66,), (99,)])

        cur.execute("SELECT id, num FROM test order by num")
        for record in cur:
         print(record)

        # Make the changes to the database persistent
        conn.commit()