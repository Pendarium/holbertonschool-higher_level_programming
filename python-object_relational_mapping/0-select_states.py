#!/usr/bin/python3
"""
This script lists all states from the MySQL database `hbtn_0e_0_usa`.

Usage:
    ./script_name.py <mysql_username> <mysql_password> <database_name>

Requirements:
    - The MySQL server must be running on localhost at port 3306.
    - The module MySQLdb must be installed (`pip install mysqlclient`).

Functionality:
    - Connects to the specified MySQL database using the provided credentials.
    - Retrieves all entries from the `states` table.
    - Sorts the results by `id` in ascending order.
    - Prints each row to stdout.

Note:
    - The script will not execute when imported as a module.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    user_name = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        password=pwd,
        db=db_name
    )

    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = mycursor.fetchall()

    for row in rows:
        print(row)

    mycursor.close()
    db.close()
