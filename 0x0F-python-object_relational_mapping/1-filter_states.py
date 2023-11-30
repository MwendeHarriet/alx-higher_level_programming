#!/usr/bin/python3
"""This script lists all states with a name starting with N
    (upper N) from the database hbtn_0e_0_usa"""


def main():
    """Main listing function"""
    import MySQLdb
    import sys
    name = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    host = "localhost"
    port = 3306
    db_connection = MySQLdb.connect(host=host, user=name, port=port,
                                    password=pwd, database=db)
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
            ORDER BY states.id ASC;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
