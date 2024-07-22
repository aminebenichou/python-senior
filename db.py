import sqlite3


conn = sqlite3.connect("todo.db")

cursor = conn.cursor()

def create_table():

    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS todoitems (id INTEGER PRIMARY KEY AUTOINCREMENT, TEXT NOT NULL);'''
    )

    conn.commit()
    print("Table created successfully")

def insertItem(item):
    cursor.execute(
        f'''INSERT INTO todoitems (TEXT) VALUES ('{item}');'''
    )
    conn.commit()


create_table()


def edit_row(id, data):
    cursor.execute(f'''
        UPDATE todoitems SET TEXT = '{data['title']}' WHERE id = {id}
    ''')

    conn.commit()



def delete_row(id):
    cursor.execute(
        f'''
            DELETE FROM todoitems WHERE id = {id}
        '''
    )
    conn.commit()



def retrieve_items():
    result = []
    rows = cursor.execute(
        f'''SELECT * FROM todoitems;'''
    )

    for row in rows:
        result.append(row)

    return result
print(retrieve_items())