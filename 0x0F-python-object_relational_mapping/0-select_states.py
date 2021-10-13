#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
import sys
if __name__ == "__main__":
        user = sys.argv[1]
        paswd = sys.argv[2]
        dbname = sys.argv[3]
        db = MySQLdb.connect(user=user, password=paswd, db=dbname)
        cur = db.cursor()
        cur.execute("SELECT id, name FROM states ORDER BY id")
        rows = cur.fetchall()
        for row in rows:
                print(row)
        db.close()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               