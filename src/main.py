import sqlite3

def connect_db():
    return sqlite3.connect('db/bakehouse_manager.db')

def add_product(name, price, stock):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", (name, price, stock))
    conn.commit()
    conn.close()

def view_products():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

if __name__ == "__main__":
    add_product("Croissant", 2.5, 50)
    add_product("Baguette", 1.5, 30)
    products = view_products()
    for product in products:
        print(product)

