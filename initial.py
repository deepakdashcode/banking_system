import mysql.connector as c

db = c.connect(host='localhost', user='<your_username>', passwd='<your_password>')
cu = db.cursor()
cu.execute('create database bank')
cu.execute('use bank')

db = c.connect(host='localhost', user='<your_username>', passwd='<your_password>', database='bank')
cu = db.cursor()
sql = 'create table information (Name varchar(100) NOT NULL ,Aadhar bigint NOT NULL  ,Account_Number bigint NOT NULL PRIMARY KEY,Balance bigint)'
cu.execute(sql)
sql1 = "insert into information VALUES ('DEFAULT',0,1000000000,0);"
cu.execute(sql1)
sql2 = r'create table banking_details (Account_number bigint NOT NULL,Status VARCHAR(1) NOT NULL,Amount BIGINT NOT NULL,Date DATE,Time TIME);'
cu.execute(sql2)

sql3='CREATE TABLE transaction_history (sender BIGINT,receiver BIGINT,Amount BIGINT,Date DATE,Time TIME);'
cu.execute(sql3)
