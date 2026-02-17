#SQL_practice.py
import sqlite3


def createTable():
    conn = sqlite3.connect('bankDB.db')

    cursor = conn.cursor()

    cursor.execute('create table customers(customerID integer primary key,' 
            'name text ,'
            'address text, email text );')

    cursor.execute('create table accounts (acc_id integer primary key, '
                   'cust_id integer, acc_type text, balance real, ' 
                   'foreign key(cust_id) '
                    'references customers(customerID));')
    
    cursor.execute('create table transactions (trans_id integer primary key, '
                   'acc_id integer, trans_type text ,'
                   ' amount real, date date, '
                    'foreign key(acc_id) '
                    'references accounts(acc_id) ); ')

    conn.commit()

    cursor.close()

    conn.close()

def insert_cust():
    conn = sqlite3.connect('bankDB.db')

    cursor = conn.cursor()
    while True:
        custno = int(input('Enter customer id as integer (99 to stop): '))
        if custno == 99 :
            break
        name = input('Enter customer name: ')
        address = input('Enter city/town: ')
        email = input('Enter email: ')
        print("\n")

        cursor.execute(f'insert into customers values({custno}, "{name}", "{address}", "{email}")')

        conn.commit()

    cursor.close()
    conn.close()

def insert_acct():
    conn = sqlite3.connect('bankDB.db')

    cursor = conn.cursor()
    while True:
        accid = int(input('Enter acc id as integer (99 to stop): '))
        if accid == 99 :
            break
        cust_id = int(input('Enter customer ID (fk): '))
        acc_type = input('Enter account type: ')
        balance = float(input('Enter balance: '))
        print("\n")

        cursor.execute(f'insert into accounts values({accid}, {cust_id}, "{acc_type}", {balance})')

        conn.commit()

    cursor.close()
    conn.close()

def insert_trans():
    conn = sqlite3.connect('bankDB.db')

    cursor = conn.cursor()
    while True:
        trans_id = int(input('Enter transaction id as integer (99 to stop): '))
        if trans_id == 99 :
            break
        acc_id = int(input('Enter account ID (fk): '))
        trans_type = input('Enter transaction type (deposit/withdrawal): ')
        amount = float(input('Enter transaction amount: '))
        ddate = input('Enter a date in Y/M/D')
        print("\n")

        cursor.execute(f'insert into transactions values({trans_id}, {acc_id}, "{trans_type}", {amount}, "{ddate}")')

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


"""
#update query
'update dept '
'set dname = "IT" '
'where deptno = 50 ;'
"""

"""
#delete query
 'delete '
 'from dept '
 'where deptno = 50 ;
 """

if __name__ == "__main__":
    # we've already created tables. if we hadn't we could launch that function here
   #insert_dept()
   #del_db()
   #select()
 #for the challenge i ran these in this order
 #   createTable()
 # insert_cust()
   # insert_acct()
    insert_trans()