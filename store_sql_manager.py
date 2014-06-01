import sqlite3

conn = sqlite3.connect("mall.db")
cursor = conn.cursor()


def create_table():
    create_query = '''create table if not exists
        stores(id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                item TEXT,
                description TEXT,
                providers_price REAL DEFAULT 0,
                selling_price REAL DEFAULT 0,
                quantity INTEGER DEFAULT 0)'''

    cursor.execute(create_query)


def add_item(name, item, description, providers_price, selling_price, quantity):
    insert_query = "insert into stores (name, item, description, providers_price, selling_price, quantity) values (?, ?, ?, ?, ?, ?)"
    cursor.execute(insert_query, (name, item, description, providers_price, selling_price, quantity))
    conn.commit()


def get_quantity(name, item):
    select_query = "SELECT quantity FROM stores WHERE name = ? AND item = ? "
    cursor.execute(select_query, (name, item))
    quantity = cursor.fetchone()
    return quantity[0]


def sell_item(name, item):
    update_query = "UPDATE stores SET quantity = ? WHERE name = ? AND item = ?"
    cursor.execute(update_query, (get_quantity(name, item) - 1, name, item))
    conn.commit()


def view_items():
    select_query = "SELECT id, name, item, description, selling_price FROM stores WHERE quantity != 0"
    result = cursor.execute(select_query)
    for row in result:
        print(row)
    return True


def view_item(id):
    select_query = "SELECT id, name, item, description, selling_price FROM stores WHERE quantity != 0 AND id = ?"
    result = cursor.execute(select_query, (id,)).fetchone()
    if result:
        print(result)
        return True
    else:
        return False


def delete_store(name):
    delete_query = "DELETE FROM stores WHERE name = ?"
    cursor.execute(delete_query, (name,))
    conn.commit()


def load_items(quantity):
    update_query = "UPDATE stores SET quantity = ? WHERE quantity = 0"
    cursor.execute(update_query, (quantity, ))
    conn.commit()
