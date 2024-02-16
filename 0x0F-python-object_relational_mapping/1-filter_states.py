#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
1. Your script should take 4 arguments:
    mysql username, mysql password, database name, and state name searched
2. You must use the module MySQLdb
3. Your script should connect to a MySQL
   server running on localhost at port 3306
4. You must use format to create the SQL query with the user input
"""


def main():
    """script Entry Point
    """
    import sys
    import MySQLdb
    USER_NAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DB_NAME = sys.argv[3]
    HOST = "localhost"
    PORT = 3306
    STATE_NAME = "N%"

    db = MySQLdb.connect(
            host=HOST,
            port=PORT,
            database=DB_NAME,
            user=USER_NAME,
            password=PASSWORD)
    qry = """
    SELECT id, name
    FROM states
    WHERE name LIKE '{}'
    ORDER BY id""".format(STATE_NAME)
    db.query(qry)
    result = db.store_result()
    for row in result.fetch_row(maxrows=0):
        print(row)
    db.close()


if __name__ == '__main__':
    main()
