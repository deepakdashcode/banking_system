import mysql.connector as c
from datetime import datetime

db = c.connect(host='localhost', user='root', passwd='2580', database='bank')
cu = db.cursor()

while True:
    account_number = int(input('Enter the account number\n'))
    sql = f'select balance from information where account_number={account_number}'
    cu.execute(sql)
    current_balance = (cu.fetchall()[0][0])
    print('Your current balance is ', current_balance)
    to_withdraw = int(input('Enter the amount you want to withdraw\n'))
    if to_withdraw > current_balance:
        print('Sorry Your balance is insufficient')
    else:
        new_amount = current_balance - to_withdraw
        sql = f'update information set balance={new_amount} where account_number={account_number}'
        cu.execute(sql)
        db.commit()
        #############
        # ADDING DATE AND TIME
        now = datetime.now()
        date_and_time = str(now).split()  # list to store current date and current time
        current_date = date_and_time[0]
        current_time = date_and_time[1]
        sql = f'insert into banking_details VALUES ({account_number},"w",{to_withdraw},"{current_date}","{current_time}")'
        cu.execute(sql)
        db.commit()
        #############
        print('Amount withdrawn =\t', to_withdraw)
        print('Remaining Balance =\t', new_amount)
