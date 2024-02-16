#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
1. Your script should take 3 arguments: mysql username,
mysql password and database name
2. You must use the module MySQLdb (import MySQLdb)
3. Your script should connect to a MySQL
server running on localhost at port 3306
4. Results must be sorted in ascending order by cities.id
5. You can use only execute() once
6. Your code should not be executed when imported
"""


def main():
    """Entry Point"""
    import sys
    import MySQLdb
    HOST = "localhost"
    PORT = 3306
    USER_NAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DB_NAME = sys.argv[3]
    db = MySQLdb.connect(
            host=HOST,
            port=PORT,
            user=USER_NAME,
            password=PASSWORD,
            database=DB_NAME)
    cur = db.cursor()
    cur.execute("""SELECT cities.id,
    cities.name,
    states.name
    FROM cities
    LEFT OUTER JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.id""")
    rows = cur.fetchmany(100)
    while rows:
        for row in rows:
            print(row)
        rows = cur.fetchmany(100)
    cur.close()
    db.close()


if __name__ == '__main__':
    main()
