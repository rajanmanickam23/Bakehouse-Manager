import sqlite3

def create_tables():
    conn = sqlite3.connect('db/bakehouse_manager.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                      product_id INTEGER PRIMARY KEY,
                      name TEXT NOT NULL,
                      price REAL NOT NULL,
                      stock INTEGER NOT NULL
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                      customer_id INTEGER PRIMARY KEY,
                      name TEXT NOT NULL,
                      email TEXT NOT NULL,
                      phone TEXT
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                      order_id INTEGER PRIMARY KEY,
                      customer_id INTEGER,
                      order_date TEXT NOT NULL,
                      total REAL NOT NULL,
                      FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS order_items (
                      order_item_id INTEGER PRIMARY KEY,
                      order_id INTEGER,
                      product_id INTEGER,
                      quantity INTEGER NOT NULL,
                      FOREIGN KEY (order_id) REFERENCES orders(order_id),
                      FOREIGN KEY (product_id) REFERENCES products(product_id)
                      )''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
