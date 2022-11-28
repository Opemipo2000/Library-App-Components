# Programmed by student F219244 on 14/11/2022

from tkinter import END
from database import Database
import pandas as pd
from datetime import datetime

database = Database("Library.db")

def loan_info():
    """ After all the values of the loan table is removed, this populates the loan table once again"""
    table_columns = ['Book_ID','Reservation_Date','Checkout_Date','Return_Date','Member_ID']
    loan_info = pd.read_csv('Loan_Reservation_History.txt', sep=",", names=table_columns, header=None, index_col=False)
    for i in range(0,446):
        book_id = loan_info['Book_ID'].tolist()[i]
        reservation_date = loan_info['Reservation_Date'].tolist()[i]
        checkout_date = loan_info['Checkout_Date'].tolist()[i]
        return_date = loan_info['Return_Date'].tolist()[i]
        member_id = loan_info['Member_ID'].tolist()[i]
        database.insert_loan_details(book_id,reservation_date,checkout_date,return_date,member_id)

def checkout_command(memberID_text,bookID_text,message):
    """ This extracts the string that was typed into both the Member ID and Book ID boxes. If the string from the member ID is between 1000-9999. All the parameters will be passed into the database where it will be inserted in a new row to checkout a book 
    
    To test this fully uncomment line 32 and comment lines 26 and 31. After you comment line 26 write member_id = memberID_text"""
    member_id = memberID_text.get()
    if int(member_id) > 999 and int(member_id) < 10000 :
        print('Hi')
        current_time = datetime.now()
        date_value = current_time.strftime("%d/%m/%Y")
        database.add_checkout(checkout_date=date_value,book_id=bookID_text.get(),member_id=member_id,message=message)
        #database.add_checkout(checkout_date=date_value,book_id=bookID_text,member_id=member_id,message=message)
    else:
        print("Bye")
        message.delete("1.0",END)
        message.insert(END,"This is not a valid member number. Member_ID number are 4 digits numbers from 1000 to 9999, please type the ID the correct way")
       # message.tag_config(END, foreground="red")

def view_checked_books(list1):
    """ Views all the book not available in the Library in the List Box"""
    list1.delete(0,END)
    for row in database.view_checkedOut_books():
        list1.insert(END,row)

if __name__ == "__main__":
    print("If the ids matches the criteria of the if statement, it will print 'Hi'. If not you'll see 'Bye'")
    print(checkout_command(1234,10,"Hello"))
    
