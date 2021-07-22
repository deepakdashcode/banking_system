import mysql.connector as c
from datetime import datetime

db = c.connect(host='localhost', user='root', passwd='2580', database='bank')
cu = db.cursor()


def get_current_balance(account_number):
    sql = f'select balance from information where account_number={account_number}'
    cu.execute(sql)
    current_balance = (cu.fetchall()[0][0])
    return current_balance


def verify_user(acc_no, aadhar):
    try:
        sql = f'select aadhar from information where account_number={acc_no}'
        cu.execute(sql)
        required_aadhar = (cu.fetchone())[0]
        if required_aadhar == aadhar:
            print('USER AUTHENTICATED')
            return True
        else:
            print('AADHAR MISMATCH !! PLEASE ENTER CORRECT AADHAR')
            return False

    except:
        print('Some ERROR OCCURRED\nMOST PROBABLY Account does not exist')
        return False


def is_valid_account(account_number, name):
    try:
        sql = f'select name from information where account_number={account_number}'
        cu.execute(sql)
        required_name = cu.fetchone()[0]
        if required_name == name:
            return True
        else:
            return False
    except:
        return False


def pay_to_account(sender_acc, receiver_acc, receiver_name, amount):
    if is_valid_account(receiver_acc, receiver_name):
        # Getting Money from sender's account
        sender_balance = get_current_balance(sender_acc)
        if sender_balance < amount:
            print('Transaction Failed due to insufficient balance')
        else:
            new_sender_balance = sender_balance - amount
            sql = f'update information set balance={new_sender_balance} where account_number={sender_acc}'
            cu.execute(sql)
            db.commit()

        ############################################
        # ADDING Money to receivers account
        current_balance = get_current_balance(receiver_acc)
        new_amount = current_balance + amount
        sql = f'update information set balance={new_amount} where account_number={receiver_acc}'
        cu.execute(sql)
        db.commit()


n = 1
while n:
    if n == 1:
        print('User Please Authenticate')
        account_number = int(input('Enter your account_number\n'))
        aadhar_number = int(input('Enter your Aadhar_number\n'))

    if n == 1:
        if verify_user(account_number, aadhar_number):
            print('Successfully verified')
        else:
            print('Invalid credentials')
            break
    n = n + 1

    print('Enter 1 to check balance')
    print('Enter 2 to pay to other account')
    print('Enter 3 to deposit money to bank')
    print('Enter 4 for transaction details')
    print('Enter 5 to logout')
    choice = int(input('Enter the choice\n'))
    if choice == 1:
        print('Your current balance is : ', get_current_balance(account_number))
    elif choice == 2:
        other_account = int(input('Enter the account to which you want to send money\n'))
        name = input('Enter the name of the person exactly as on CARD\n')
        if is_valid_account(other_account, name):
            amount = int(input('Enter the amount you want to send\n'))
            if amount<0:
                print('INVALID AMOUNT')
                break
            pay_to_account(account_number, other_account, name, amount)
            now = datetime.now()
            date_and_time = str(now).split()  # list to store current date and current time
            current_date = date_and_time[0]
            current_time = date_and_time[1]
            sql = f'INSERT INTO transaction_history VALUES ({account_number},{other_account},{amount},"{current_date}","{current_time}")'
            cu.execute(sql)
            db.commit()
            print('TRANSACTION COMPLETED SUCCESSFULLY')
        else:
            print('Please enter a valid account Number and name')
    elif choice == 3:
        from deposit_money import start

        start()
    elif choice == 4:
        sql=f'select * from transaction_history where sender={account_number} or receiver={account_number}'
        cu.execute(sql)
        x = cu.fetchall()
        for i in x:
            print('Sender =', i[0])
            print('Receiver =', i[1])
            print('Amount =', i[2])
            print('Date :', i[3])
            print('Time :', i[4])
            print('\n' * 5)

    elif choice == 5:
        n = 1
        print('\n'*50)
