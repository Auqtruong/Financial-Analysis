from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect("business.db")
    conn.row_factory = sqlite3.Row
    
    cursor = conn.cursor()
    cursor.execute('''
                   SELECT ROWID, Company, FORMAT('$%,d', Capital) as Capital, transaction_type, transaction_date
                   FROM transactions
                   WHERE transaction_date = '2024'
                   ''')
    
    rows = cursor.fetchall()

    conn.close()  
    
    return render_template("home.html", rows=rows)

if __name__ == '__main__':
    app.run()