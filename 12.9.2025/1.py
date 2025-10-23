"""import mariadb
print(mariadb.__version__)
print("Successfully connected to MariaDB")"""

"""import mariadb
connection = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='baoloc123',
    database='people1',
    autocommit=True
)
print("Connected to MariaDB successfully")

def get_employees_by_last_name(connection, last_name):
    sql= "select number,Last_name,First_name,Salary from Employee1 where Last_name = ?"
    cursor = connection.cursor()
    cursor.execute(sql, (last_name,))
    result = cursor.fetchall()
    if result:
        for row in result:
            print(f"Hello!I am {row[2]} {row[1]}. My salary is {row[3]} euros per month.")
    else:
        print(f"No employees with last name {last_name} found.")
    cursor.close()
ln=input("Enter the last name of the employee whose salary you wish to check: ")
get_employees_by_last_name(connection, ln)
connection.close()
print("Connection closed")"""

"""import mariadb
connection = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='baoloc123',
    database='people1',
    autocommit=True
)
def update_salary(connection, number, new_salary):
    sql = "Update Employee1 set Salary = ? where Number = ?"
    cursor = connection.cursor()
    cursor.execute(sql, (new_salary, number))
    connection.commit()
    if cursor.rowcount != 0:
        print("Salary updated successfully!")
    else:
        print("No employee with number {number} found.")
number = input("Enter the number: ")
new_salary = input("Enter the new salary: ")
update_salary(connection, number, new_salary)
connection.close()
print("Connection closed")"""



