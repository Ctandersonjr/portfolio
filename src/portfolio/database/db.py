import psycopg


def get_conn() -> psycopg.Connection:
    return psycopg.connect(
        "postgresql://postgres:Anderson2345@localhost:5432/portfolio",
    )
conn = get_conn()




def init_table() -> None:
    sql_command = """
    CREATE TABLE IF NOT EXISTS test (
        username INT Primary Key,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    );
    """
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(sql_command)
    conn.commit()
    conn.close()
