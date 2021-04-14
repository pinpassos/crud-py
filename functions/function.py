# Import modules
import mysql.connector
from functions import connect
import dotenv
import os

# Dotenv config
dotenv.load_dotenv(dotenv.find_dotenv())
password = os.getenv('user_password')

# Functions
def menu():
    print('{:^60}'.format("SYSTEM 33"))
    print('=-' * 30)
    print('''        [1] - Change user password.
        [2] - Verify if user exists in system33.
        [3] - Close application.''')
    print('=-' * 30)

def changePassword(login_user):
    try:
        mycursor = connect.mydb.cursor()
        sql = f'UPDATE usuario SET senha = "{password}" WHERE login = {login_user}'
        mycursor.execute(sql)
    except Exception as err:
        print(f'MySQL Error:',err)
    else:
        connect.mydb.commit()
        if mycursor.rowcount > 0:
            print(mycursor.rowcount, 'Row affected - Password changed successfully.')
        else:
            sql = 'SELECT senha FROM usuario WHERE login = {}'.format(login_user)
            mycursor.execute(sql)
            myresult = mycursor.fetchmany(1)
            if len(myresult) == 0:
                print('User not found.')
            elif myresult[0][0] == password:
                print(mycursor.rowcount - 1, 'Row affected - Password is already default.')

def checkUser(login_user):
    try:
        mycursor = connect.mydb.cursor()
        sql = f'SELECT login FROM usuario WHERE login = {login_user}'
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
    except Exception as err:
        print('User not found, error: ', err)
        return False
    else:
        print('User:', myresult[0], 'is in MySQL database')