# Import modules
import mysql.connector
from functions import function
from functions import connect
from time import sleep

# Main
while True:
    
    function.menu()
    try:
        option = int(input('\nType option number: '))
    except ValueError:
        print('Error: Input a valid number.')
    else:
        if option == 1:
            print('\nUpdating password...')
            login_user = str(input('Input the register number: '))
            function.changePassword(login_user)
            print("\n")

        elif option == 2:
            print('\nSearching for register in MySQL database... ')
            login_user = str(input('input the register number: '))
            function.checkUser(login_user)
            print("\n")
            
        elif option == 3:
            print('\nClosing application...')
            sleep(3)
            break

        else:
            print('Type a valid option.\n')
