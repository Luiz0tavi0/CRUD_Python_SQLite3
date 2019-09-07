import sqlite3

def commit_close(func):
    def decorator(*args):
        con = sqlite3.connect('base.db')
        cur = con.cursor()
        sql = func(*args)
        cur.execute(sql)
        con.commit()
        con.close()
    return decorator

sql = '''CREATE TABLE IF NOT EXISTS users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL)'''


@commit_close
def db_insert(name, phone, email):
    return "INSERT INTO users(name, phone, email)" \
           "VALUES('{}','{}','{}')".format(name, phone, email)


@commit_close
def db_update(name, email):
    return "UPDATE users SET name = '{}' WHERE email = '{}'".format(name, email)


@commit_close
def db_delete(email):
    return "DELETE FROM users WHERE email = '{}'".format(email)


def db_delete_all(reset_table= False):
    con = sqlite3.connect('base.db')
    cur = con.cursor()
    cur.execute("DELETE FROM users;")
    if reset_table: cur.execute("DELETE FROM sqlite_sequence WHERE name='users';")
    con.commit()
    con.close()

def db_select(field, data):
    con = sqlite3.connect('base.db')
    cur = con.cursor()
    sql = '''SELECT id, name, phone,email FROM users WHERE {} = {}'''.format(field,data)
    cur.execute(sql)
    data = cur.fetchall()
    con.close()
    return data


