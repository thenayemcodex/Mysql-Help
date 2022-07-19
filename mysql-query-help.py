
try:
  # Install mysql-connecor using pip $ pip3 install mysql-connector and then Import as shown below.
	import mysql.connector
except:
	print('Failed to Import Mysql.connector')
	


# Connecting With database.......................................................................
mydb = mysql.connector.connect(host = "localhost", user = "mysql-username", passwd = "mysql-password",database="mysql-database-name")
print('Connected')

# Creating Cursor for handle Data ...............................................................
mycursor = mydb.cursor()

# Creating Database .............................................................................
mycursor.execute("CREATE DATABASE if not exists mydatabase")
print('Database Created')

# Show All databases ............................................................................
mycursor.execute("SHOW DATABASES")

for x in mycursor:
	print(x) 

# Creating Table into database ..................................................................
mycursor.execute("CREATE TABLE if not exists customers (name VARCHAR(255), address VARCHAR(255))")

try:
	# Adding Primary Key column into data Table..................................................
	mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") 
except:
	pass

print('table created ')  

#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT , name VARCHAR(255), address VARCHAR(255))") 
# For create table with id at once ..............................................................

# Inserting Data into Table .....................................................................
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("nayem", "Highway 21")
mycursor.execute(sql, val)

print(mycursor.rowcount, "record inserted.")

# Fetching / Selecting data from table ..........................................................
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# Fetching / selecting a unique value from the data tabel .......................................
sql = "SELECT * FROM customers WHERE address ='Highway 21'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x[0],x[1],x[2])


# Updating an unique column or data row .........................................................
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Highway 21'"

mycursor.execute(sql)
print('data updated')

# Filtering data by column name .................................................................
sql = "SELECT * FROM customers ORDER BY name "

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x) 
print('Fetched By name')

# Deleting an unique value or a row from database ...............................................
sql = "DELETE FROM customers WHERE address = 'Highway 21'"

mycursor.execute(sql)


print(mycursor.rowcount, "record(s) deleted")



# Deleting Table from database ..................................................................
sql = "DROP TABLE customers"

mycursor.execute(sql) 


# Saving data table after the queries ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
mydb.commit()

# Closing the database after saving data into the database /...................................
mydb.close()
