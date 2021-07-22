import mysql.connector as c
from main import *

db = c.connect(host='localhost', user='root', passwd='2580', database='bank')
cu = db.cursor()
while True:
    name = input('Enter your name\n')
    aadhar = int(input('Enter the aadhar number\n'))
    initial_amount = int(input('Enter the initial amount\n'))

    sql = "select max(Account_Number) from information;"
    cu.execute(sql)
    current_max = (cu.fetchall()[0][0])
    current_account_number = current_max + 1
    acc = account(name, aadhar,current_account_number,initial_amount)

    sql=f'insert into information VALUES ("{name}",{aadhar},{current_account_number},{initial_amount})'
    cu.execute(sql)
    db.commit()

    print('\n\nACCOUNT CREATED SUCCESSFULLY!!!!!!!\n\nNOTE YOUR ACCOUNT NUMBER\n')
    print(acc)

    if input('Enter q to exit\n').lower().strip()[0]=='q':
        break
    else:
        continue

print('Thank You for registering in IICI BANK')