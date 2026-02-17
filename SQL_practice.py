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



def insert_dept():
    conn = sqlite3.connect('univ2.db')

    cursor = conn.cursor()
    deptno = 0
    while deptno != 99:
        deptno = int(input('Enter deptno as integer (99 to stop): '))

        dname = input('Enter dept. name: ')
        print("\n")

        cursor.execute(f'insert into dept values({deptno}, "{dname}")')

        conn.commit()
    cursor.close()
    conn.close()


def del_db():
    conn = sqlite3.connect('univ2.db')

    cursor = conn.cursor()
    
       # deptno = int(input('Enter deptno as integer (99 to stop): '))

       # dname = input('Enter dept. name: ')
       # print("\n")

    cursor.execute('delete from dept ;')

    conn.commit()
    cursor.close()
    conn.close()




if __name__ == "__main__":
    # we've already created tables. if we hadn't we could launch that function here
   insert_dept()
   #del_db()


