#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa:
1. take 3 arguments: mysql username, mysql password and
   database name (no argument validation needed)
2. use the module MySQLdb (import MySQLdb)
3. connect to a MySQL server running on localhost at port 3306
4. Results must be sorted in ascending order by states.id
5. Your code should not be executed when imported.
"""


def main():
    """Open a connection to database and retrieve all states
    """
    import sys
    import MySQLdb
    HOST = "localhost"
    PORT = 3306
    USER_NAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DB = sys.argv[3]
    conn = MySQLdb.connect(
            host=HOST,
            port=PORT,
            user=USER_NAME,
            password=PASSWORD,
            database=DB)
    conn.query("""SELECT id, name FROM states ORDER BY id""")
    result = conn.store_result()
    rows = result.fetch_row(maxrows=0)
    for row in rows:
        print(row)
    conn.close()


if __name__ == '__main__':
    main()
