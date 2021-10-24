from db_migrations import connect_db, create_cursor, commit_db, close_cursor, close_db


def create_task(task, description, date):
    conn = connect_db()
    cur = create_cursor(conn)

    res = cur.execute("INSERT INTO task (task, description, date) VALUES(%s,%s,%s)", (task, description, date))
    # Make the changes to the database persistent
    conn = commit_db(conn)
    # Close communication with the database
    close_cursor(cur)
    close_db(conn)
    return res


def get_task_list():
    conn = connect_db()
    cur = create_cursor(conn)

    res = cur.execute("SELECT * FROM task;")
    # Make the changes to the database persistent
    conn = commit_db(conn)
    # Close communication with the database
    close_cursor(cur)
    close_db(conn)
    return res
