import mysql.connector
from getpass import getpass

# Database connection configuration
db_config = {
    "host": "localhost",      # Change to your host, e.g., '127.0.0.1'
    "user": "root",           # Your MySQL username
    "password": "your_mysql_password",  # Your MySQL password
    "database": "your_database_name"    # The database containing the users table
}

# Connect to the MySQL database
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")
    exit(1)

# Get user input
username = input("Enter your username: ")
password = getpass("Enter your password: ")  # hides input for password

# Query to check credentials
query = "SELECT * FROM users WHERE username = %s AND password = %s"
cursor.execute(query, (username, password))

result = cursor.fetchone()

if result:
    print("Login Successful")
else:
    print("Login Failed")

cursor.close()
conn.close()
