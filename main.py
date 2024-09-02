import sqlite3

def create_table():
    try:
        conn = sqlite3.connect("business.db")

        cursor  = conn.cursor()

        cursor.execute("DROP TABLE IF EXISTS transactions")

        table = """ CREATE TABLE IF NOT EXISTS transactions (
                    Company          TEXT         NOT NULL,
                    Capital          BIGINT       NOT NULL,
                    Transaction_Type TEXT         NOT NULL,
                    Transaction_Date YEAR
                ); """
                
        cursor.execute(table)

        cursor.execute("INSERT INTO transactions VALUES ('PepsiCo',                     2250000000,     'Debt', '2024')")
        cursor.execute("INSERT INTO transactions VALUES ('Allstate',                    500000000,      'Debt', '2024')")
        cursor.execute("INSERT INTO transactions VALUES ('GM Financial',                2500000000,     'Debt', '2024')")
        cursor.execute("INSERT INTO transactions VALUES ('Hyatt Inc',                   800000000,      'Debt', '2024')")
        cursor.execute("INSERT INTO transactions VALUES ('Morgan Stanley Bank',         2750000000,     'Debt', '2024')")
        cursor.execute("INSERT INTO transactions VALUES ('Comcast',                     3250000000,     'Debt', '2024')")
        cursor.execute("INSERT INTO transactions VALUES ('JPMorgan',                    9000000000,     'Debt', '2024')")
        cursor.execute("INSERT INTO transactions VALUES ('Adobe Inc',                   2000000000,     'Debt', '2024')")
        cursor.execute("INSERT INTO transactions VALUES ('Humana',                      2250000000,     'Debt', '2024')")
        cursor.execute("INSERT INTO transactions VALUES ('Southern California Edison',  1600000000,     'Debt', '2024')")
        cursor.execute("INSERT INTO transactions VALUES ('Pacific Gas & Electric',      2250000000,     'Debt', '2024')")
        cursor.execute("INSERT INTO transactions VALUES ('AstraZeneca',                 5000000000,     'Debt', '2024')")
        cursor.execute("INSERT INTO transactions VALUES ('Eli Lilly',                   6500000000,     'Debt', '2024')")
        cursor.execute("INSERT INTO transactions VALUES ('NextEra Energy',              4400000000,     'Debt', '2024')")
        cursor.execute("INSERT INTO transactions VALUES ('Charter Communications',      2000000000,     'Debt', '2023')")
        cursor.execute("INSERT INTO transactions VALUES ('McDonald''s Corp',            2000000000,     'Debt', '2023')")
        cursor.execute("INSERT INTO transactions VALUES ('Lockheed Martin',             2000000000,     'Debt', '2023')")
        cursor.execute("INSERT INTO transactions VALUES ('Apple Inc',                   5250000000,     'Debt', '2023')")
        cursor.execute("INSERT INTO transactions VALUES ('Merck',                       6000000000,     'Debt', '2023')")
        cursor.execute("INSERT INTO transactions VALUES ('Amgen',                       24000000000,    'Debt', '2023')")

        cursor.execute("INSERT INTO transactions VALUES ('Lineage Inc',                                                         5102319924,    'Equity', '2024')")
        cursor.execute("INSERT INTO transactions VALUES ('OneStream',                                                           563500000,     'Equity', '2024')")
        cursor.execute("INSERT INTO transactions VALUES ('BrightView Holdings',                                                 227500000,     'Equity', '2024')")
        cursor.execute("INSERT INTO transactions VALUES ('UL Solutions',                                                        946400000,     'Equity', '2024')")
        cursor.execute("INSERT INTO transactions VALUES ('Mobileye Global',                                                     1690500000,    'Equity', '2023')")
        cursor.execute("INSERT INTO transactions VALUES ('Gates Industrial',                                                    304031250,     'Equity', '2023')")
        cursor.execute("INSERT INTO transactions VALUES ('Laureate Education',                                                  320211284,     'Equity', '2022')")
        cursor.execute("INSERT INTO transactions VALUES ('Mobileye Global',                                                     8610000000,    'Equity', '2022')")
        cursor.execute("INSERT INTO transactions VALUES ('Rivian Automotive Inc',                                               13724100000,   'Equity', '2021')")
        cursor.execute("INSERT INTO transactions VALUES ('Weber',                                                               297499996,     'Equity', '2021')")
        cursor.execute("INSERT INTO transactions (company, capital, transaction_type) VALUES ('Meta',                           18408000000,   'Equity')")
        cursor.execute("INSERT INTO transactions (company, capital, transaction_type) VALUES ('Remitly Global',                 522999411,     'Equity')")
        cursor.execute("INSERT INTO transactions (company, capital, transaction_type) VALUES ('MetLife',                        6330000000,    'Equity')")
        cursor.execute("INSERT INTO transactions (company, capital, transaction_type) VALUES ('CBOE',                           390195000,     'Equity')")
        cursor.execute("INSERT INTO transactions (company, capital, transaction_type) VALUES ('Academy Sports and Outdoors',    515200000,     'Equity')")
        cursor.execute("INSERT INTO transactions (company, capital, transaction_type) VALUES ('AIG',                            8700000000,    'Equity')")
        cursor.execute("INSERT INTO transactions (company, capital, transaction_type) VALUES ('General Motors',                 18140000000,   'Equity')")
        cursor.execute("INSERT INTO transactions (company, capital, transaction_type) VALUES ('American Water',                 1247000000,    'Equity')")
        cursor.execute("INSERT INTO transactions (company, capital, transaction_type) VALUES ('Hertz',                          1320000000,    'Equity')")
        cursor.execute("INSERT INTO transactions (company, capital, transaction_type) VALUES ('US Foods Holding',               1299500000,    'Equity')")

        conn.commit()

        conn.close()
        
    except sqlite3.Error as e:
        print(e)

if __name__ == '__main__':
    create_table()