import psycopg2


def connect_db():
    # Connect to an existing database
    conn = psycopg2.connect(database="tododb", user="todoadmin", password="todoadmin", host='localhost', port=5432)
    return conn


def create_cursor(conn):
    # Open a cursor to perform database operations
    cur = conn.cursor()
    return cur


def commit_db(conn):
    conn.commit()
    return conn


def close_cursor(cur):
    cur.close()


def close_db(conn):
    conn.close()


def create_tables():
    conn = connect_db()

    cur = create_cursor(conn)
    # Execute a command: this creates a new table
    cur.execute(
        "CREATE TABLE task (id serial PRIMARY KEY, task varchar(255) NOT NULL, description text NOT NULL , date  timestamp);")
    cur.execute(
        "CREATE TABLE meeting (id serial PRIMARY KEY, person varchar(255) NOT NULL, purpose text NOT NULL , date  timestamp);")

    # Make the changes to the database persistent
    conn = commit_db(conn)

    # Close communication with the database
    close_cursor(cur)
    close_db(conn)


if __name__ == '__main__':
    create_tables()
