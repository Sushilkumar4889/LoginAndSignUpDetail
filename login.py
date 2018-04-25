
#open pyxl
import time
import datetime
import openpyxl
import smtplib,time,xlrd,xlwt
wb = xlwt.Workbook()
ws = wb.add_sheet("login")
input_open = int(input('enter your choice'))
if input_open == 1:
    print("enter your detail to sign up")
    first_name = input('enter your first name')
    last_name = input('enter your last name')
    '''date_of_birth = datetime.date(input('enter DOB'))
    try:
        date_of_birth = datetime.date(date_of_birth)
    except:
        pass
    #mob_no = int(input('enter mob no'))
    #if len(mob_no) < count(10):
     #   print("please enter 10 digit mob no")'''
    address = input()
    UserName = input("enter the username to login into your accout")
    try:
        val=int(val)
    except:
        pass
    print('enter your username and password to log in')
    PassWord = input("Now please create a password. ")

    file = open("Login.xls","a")
    file.write (UserName)
    file.write (",")
    file.write (PassWord)
    file.write("\n")
    file.close()

    print ("Your login details have been saved. ")

else:
    registered_users = read('Login.xls')
    username = input("enter the username to login into your accout")
    try:
        val=int(val)
    except:
        pass
    print('enter your username and password to log in')
    password = input("Now please create a password. ")
    
    logged_in = False
with open('Login.txt', 'r') as file:
    for line in file:
        username, password = line.split(',')
        if usr_pass_registered(username, password, registered_users):
            print('successfully logged in')
        else:
            print('username or password is incorrect')
    
    
    
