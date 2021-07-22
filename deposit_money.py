import mysql.connector as c
from datetime import datetime

db = c.connect(host='localhost', user='root', passwd='2580', database='bank')
cu = db.cursor()


def start():
    while True:
        account_number = int(input('Enter the account number\n'))
        sql = f'select balance from information where account_number={account_number}'
        cu.execute(sql)
        current_balance = (cu.fetchall()[0][0])
        print('Your current balance is ', current_balance)
        to_deposit = int(input('Enter the amount you want to deposit\n'))
        new_amount = current_balance + to_deposit
        sql = f'update information set balance={new_amount} where account_number={account_number}'
        cu.execute(sql)
        db.commit()
        ################
        # ADDING DATE AND TIME
        now = datetime.now()
        date_and_time = str(now).split()  # list to store current date and current time
        current_date = date_and_time[0]
        current_time = date_and_time[1]
        sql = f'insert into banking_details VALUES ({account_number},"d",{to_deposit},"{current_date}","{current_time}")'
        cu.execute(sql)
        db.commit()
        ################
        print('Amount deposited =\t', to_deposit)
        print('Current Balance =\t', new_amount)

if __name__=='__main__':
    start()