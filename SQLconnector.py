# =============================================================================
# import mysql.connector 
# mydb=mysql.connector.connect(host="local host",user="root",passwd="rajeev117",db="")
# mycursor.execute("show dtabases")
# for db in mycursor:
#     print(db)
# 
# =============================================================================
#import mysql.connector as msc
#mydb=msc.connect(host="localhost",user="root",passwd="rajeev117",db="items")
#mycursor = mydb.cursor()
#mycursor.execute("select * from catagory where name=='stockable'")
#for db in mycursor:
#    print(db)
def menu():
    import mysql.connector as msc
    mydb = msc.connect(host="localhost", user="root", passwd="rajeev117", db="company")
    mycursor = mydb.cursor()
    # mycursor.execute('use company')
    a=int(input("""1. Initialize/Reconfigure Database Schema
a. Create a database if it doesn’t exist
b. Create a table if it doesn’t exist
2. Display the structure of the table
3. Insert n records into the table.(Accept number of records n and the data values
from the user) 
4. Modify a record based on a criteria entered by the user
5. Display all the records
6. Display records based on a criteria entered by the user
7. Delete all records or the records based on a criteria entered by the user
8. Exit"""))
    if a==1:
        b=input("enter database name")
        c='use %s'%(b)
        mycursor.execute(c)
        a=int(input('Enter next operation'))
        if a== 2:
            d=input('Enter table name')
            e='desc %s'%(d)
            mycursor.execute(e)
            a=int(input('Enter next operation'))
        if a==3:
            x=int(input('enter no of records to be entered'))
            for i in range(x):
                mycursor.execute('input %s'%d 'values())
                  
        if a==4:
            mycursor.execute("update table")
        if a==5:
            d=input('Enter table name')
            z='select * from %s'%(d)
            mycursor.execute(z)
        if a== 6:
            mycursor.execute("select * from table")
        if a==7:
            x=input('enter table to be droped')
            z= 'drop table' + x + 'from company'
            mycursor.execute(z)
        if a==8:
            mycursor.execute('exit')
    for db in mycursor:
        print(db)

