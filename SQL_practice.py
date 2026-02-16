#SQL_practice.py
import sqlite3


def createTable():
    conn = sqlite3.connect('univ2.db')

    cursor = conn.cursor()

    cursor.execute('create table dept(deptno integer primary key,' 
            'dname text)')

    cursor.execute('create table students (roll integer primary key,' 
                'name text,'
                'city text,'
                    'deptno integer,'
                    'foreign key(deptno)'
                    'references dept(deptno))')

    conn.commit()

    cursor.close()

    conn.close()




conn = sqlite3.connect('univ2.db')

cursor = conn.cursor()
cursor.execute('insert into dept calues(10, "CSE")')
conn.commit()
cursor.close()
conn.close()
