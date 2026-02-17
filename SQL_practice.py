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
    while True:
        deptno = int(input('Enter deptno as integer (99 to stop): '))
        if deptno == 99 :
            break
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

    cursor.execute('delete from dept where(deptno = 99) ;')

    conn.commit()
    cursor.close()
    conn.close()

def select():
    conn = sqlite3.connect('univ.db')

    cursor = conn.cursor()

    #challenge no. 1
    #strSQL = 'select city from students group by city ;'
    #solution 'select distinct city from students'
    #challenge no. 2
    #strSQL = 'select name from students, dept where(students.deptno = dept.deptno and dept.dname="CSE");'

    #challenge no. 3
    #strSQL = 'select name from students, dept where(students.deptno = dept.deptno and students.city <> "MUM" and dept.dname = "Civil");'
    #solution  'select  * from students where deptno = 30 except select * from students where city="MUM" '
    #challenge no. 4
    #strSQL = 'select count(name), (city) from students, dept where(students.deptno = dept.deptno and dept.dname = "ECE") group by students.city ;'
    
    #challenge no. 5 - subquery
    #strSQL = 'select count(students.deptno), dept.dname from students, dept ' \
    'where (students.deptno = dept.deptno and count(students.deptno)>' \
    '(select count(students.name) from students, dept ' \
    'where (students.deptno = dept.deptno and dept.dname = "ECE") ));'

    #solution
    strSQL = 'select deptno, count(*) from students '  \
    'group by deptno ' \
    'having count(*) > (select count(*) from students where deptno = 20) ;'

    #he 'cheats' and uses deptno in teh students table where clause to 
    #select the deptno he is interetested in
    
    tuples = cursor.execute(strSQL)

    for t in tuples:
        print(t)

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    # we've already created tables. if we hadn't we could launch that function here
   #insert_dept()
   #del_db()
   select()


