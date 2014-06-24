import sqlite3

conn = sqlite3.connect("mall.db")
cursor = conn.cursor()


def create_table():
    create_query = """create table if not exists
        stores(id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            item TEXT,
            description TEXT,
            providers_price REAL DEFAULT 0,
            selling_price REAL DEFAULT 0,
            quantity INTEGER DEFAULT 0)"""

    cursor.execute(create_query)


def add_item(name,
             item,
             description,
             providers_price,
             selling_price,
             quantity):

    insert_query = """INSERT into stores
    (name, item, description, providers_price, selling_price, quantity)
     values (?, ?, ?, ?, ?, ?)"""

    cursor.execute(
        insert_query,
        (name, item, description, providers_price, selling_price, quantity)
    )
    conn.commit()


def get_quantity(name, item):
    select_query = "SELECT quantity FROM stores WHERE name = ? AND item = ? "
    cursor.execute(select_query, (name, item))
    quantity = cursor.fetchone()
    return quantity[0]


def get_price(name, item):
    select_query = """SELECT selling_price
                      FROM stores
                      WHERE name = ? AND item = ? """
    cursor.execute(select_query, (name, item))
    price = cursor.fetchone()
    return price[0]


def sell_item(name, item):
    update_query = "UPDATE stores SET quantity = ? WHERE name = ? AND item = ?"
    cursor.execute(update_query, (get_quantity(name, item) - 1, name, item))
    conn.commit()


def view_items(name):
    select_query = """SELECT id, item, description, selling_price
                      FROM stores
                      WHERE quantity != 0 AND name = ?"""
    result = cursor.execute(select_query, (name, ))
    for row in result:
        print(row)
    return True


def view_item(name, id):
    select_query = """SELECT id, item, description, selling_price FROM
                   stores WHERE quantity != 0 AND name = ? AND id = ?"""
    result = cursor.execute(select_query, (name, id)).fetchone()
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


def create_staff_table():
    create_query = """create table if not exists
        staff(name TEXT,
            username TEXT,
            password TEXT)"""

    cursor.execute(create_query)


def get_staff_information(name):
    select_query = "SELECT username, password FROM staff WHERE name = ?"
    result = cursor.execute(select_query, (name, )).fetchone()
    return result


def add_staff_information(name, username, password):
    insert_query = """INSERT into staff (name, username, password)
                      values (?, ?, ?)"""
    cursor.execute(insert_query, (name, username, password))
    conn.commit()
