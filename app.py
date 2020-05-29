import sqlite3 as sq


def index():
    conn = sq.connect('data.db')
    c = conn.cursor()
    
    try:
        c.execute("""
	    CREATE TABLE products (
		    name TEXT,
		    much INT
	     );
	    """)
    except:
        pass

    return 'OK'
         


def add():
    while True:
        prod_name = request.form['prod_name']
        quant = request.form['quant']
        conn = sq.connect('data.db')
        c = conn.cursor()
        c.execute("""
	    INSERT INTO products (name, much) VALUES (
	    (?, ?)
	    )
	    """, (prod_name, quant))
        c.commit()
    return render_template('add.html')

def view():
    conn = sq.connect('data.db')
    c = conn.cursor()
    c.execute("""
        SELECT * FROM products
    """)
