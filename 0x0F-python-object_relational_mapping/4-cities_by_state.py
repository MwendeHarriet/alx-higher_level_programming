#!/usr/bin/python3
"""This script script that lists all cities from the database hbtn_0e_4_usa"""


def main():
    """Main function"""
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
    query = "SELECT cities.id, cities.name, states.name \
            FROM cities LEFT JOIN states \
            ON cities.state_id = states.id \
            ORDER BY cities.id"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
