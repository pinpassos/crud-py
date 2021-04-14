# Import modules
import mysql.connector
import dotenv
import os

# Dotenv config
dotenv.load_dotenv(dotenv.find_dotenv())
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')

# Database connection
try:
    mydb = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )
except mysql.connector.Error as err:
    print('Error connection:', err)
else:
    print('Conection estabelished!')
