import sqlite3

conn = sqlite3.connect("mall.db")
cursor = conn.cursor()


def create_table():
    create_query = """create table if not exists
        establishments(id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            restaurant_cafe TEXT,
            item TEXT,
            ingredients TEXT,
            price REAL DEFAULT 0,
            gr_ml INTEGER DEFAULT 0)"""

    cursor.execute(create_query)


def add_item(name,
             type,
             item,
             ingredients,
             price,
             grams):

    insert_query = """INSERT into establishments
    (name, restaurant_cafe, item, ingredients, price, gr_ml)
     values (?, ?, ?, ?, ?, ?)"""

    cursor.execute(
        insert_query,
        (name, type, item, ingredients, price, grams)
    )
    conn.commit()


def view_items(name):
    select_query = """SELECT item, ingredients, price, gr_ml
                      FROM establishments
                      WHERE name = ?"""
    result = cursor.execute(select_query, (name, ))
    for row in result:
        print(row)
    return True


def get_price(name, item):
    select_query = """SELECT price
                      FROM establishments
                      WHERE name = ? AND item = ? """
    cursor.execute(select_query, (name, item))
    price = cursor.fetchone()
    return price[0]


def view_item(name, id):
    select_query = """SELECT * FROM establishments WHERE id = ? AND name = ?"""
    result = cursor.execute(select_query, (id, name)).fetchone()
    if result:
        print(result)
        return True
    else:
        return False


def delete_establishment(name):
    delete_query = "DELETE FROM establishments WHERE name = ?"
    cursor.execute(delete_query, (name,))
    conn.commit()
