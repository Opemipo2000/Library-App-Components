# Programmed by student F219244 on 14/11/2022

from database import Database
from tkinter import END
from datetime import datetime

database = Database("Library.db")

def view_available_books(list1):
    """ Shows all the books that are available for checkout in the List Box"""
    list1.delete(0,END)
    for row in database.view_available_books():
        list1.insert(END,row)

def return_command(memberID_text,bookID_text,message):
    """ This extracts the string that was typed into both the Member ID and Book ID boxes. If the string from the member ID is between 1000-9999. All the parameters will be passed into the database where it will be inserted in a new row to checkout a book 
    
    To test this fully uncomment line 26 and comment lines 19 and 25. After you comment line 26 write member_id = memberID_text"""
    member_id = memberID_text.get()
    print(type(member_id))
    if int(member_id) > 999 and int(member_id) < 10000:
        print("Hi")
        current_time = datetime.now()
        date_value = current_time.strftime("%d/%m/%Y")
        #database.add_return(return_date=date_value,book_id=bookID_text.get(),member_id=member_id,message=message)
        database.add_return(return_date=date_value,book_id=bookID_text.get(),member_id=member_id,message=message)
        message.delete("1.0",END)
        message.insert(END,"Return of Book is Successful!!!!")
    else:
        print("Bye")
        message.delete("1.0",END)
        message.insert(END,"This is not a valid member number. Member_ID number are 4 digits numbers from 1000 to 9999, please type the ID the correct wa")

if __name__ == "__main__":
    print("If the ids matches the criteria of the if statement, it will print 'Hi'. If not you'll see 'Bye'")
    print(return_command(1395,100,"Hello"))