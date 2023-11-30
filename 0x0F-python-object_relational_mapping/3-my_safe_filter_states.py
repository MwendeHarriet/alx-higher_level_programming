#!/usr/bin/python3
"""This script takes in arguments and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument which is safe
    from MySQL injections"""


def main():
    """Main function"""
    import MySQLdb
    import sys
    name = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    tgt = sys.argv[4]
    host = "localhost"
    port = 3306
    db_connection = MySQLdb.connect(host=host, user=name, port=port,
                                    password=pwd, database=db)
    cursor = db_connection.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY \
            %s ORDER BY states.id ASC;"
    cursor.execute(query, (tgt,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
