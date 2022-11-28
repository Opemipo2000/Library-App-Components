# Programmed by student F219244 on 14/11/2022

import sqlite3
from tkinter import END

class Database:

    def __init__(self, db):
        """ This function creates two tables called book and loan which would hold the values from Book_Info.txt and Loan_Reservation.txt respectively """
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (ID text, Genre text, Title text, Author text, Purchase_price text, Purchase_date text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS loan (Book_ID text, Reservation_Date text,  Checkout_Date text, Return_Date text, Member_ID text)")
        self.conn.commit()

    def insert(self,id_number,genre,title,author,purchase_price,purchase_date):
        """ This insert the parameters provided into there allocated column in the book table """
        self.cur.execute("INSERT INTO book VALUES (?,?,?,?,?,?)",(id_number,genre,title,author,purchase_price,purchase_date))
        self.conn.commit()

    def insert_loan_details(self,book_id,reservation_date,checkout_date,return_date,member_id):
        """ This insert the parameters provided into there allocated column in the loan table """
        self.cur.execute("INSERT INTO loan VALUES (?,?,?,?,?)",(book_id,reservation_date,checkout_date,return_date,member_id))
        self.conn.commit()

    def view(self):
        """ Retrieves all the rows of data from the book table and sends it of to be printed """
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def view_checkedOut_books(self):
        """ Retrieves all the rows of the book table which the condition that there is data in the checkout date column and no data in the return date column """
        self.cur.execute("SELECT book.*,loan.Member_ID FROM book INNER JOIN loan ON book.ID = Book_ID WHERE (Checkout_Date IS NOT NULL AND Return_date IS NULL) ORDER BY Member_ID DESC")
        rows=self.cur.fetchall()
        return rows

    def view_available_books(self):
        """ Retrieves all the rows of the book table that does have the condition such as data in the checkout date column and no data in the return date column """
        self.cur.execute("SELECT * FROM book WHERE ID NOT IN (SELECT loan.Book_ID FROM loan WHERE (Checkout_Date IS NOT NULL AND Return_date IS NULL) ORDER BY Member_ID DESC) ORDER BY ID DESC")
        rows=self.cur.fetchall()
        return rows

    def search(self,title=""):
        """ Return all the rows the contain the sting passed by the title parameter"""
        self.cur.execute("SELECT * FROM book WHERE Title LIKE ? ",('%'+title+'%',))
        rows = self.cur.fetchall()
        return rows

    def add_checkout(self,book_id="",checkout_date="",member_id="",message=""):
        """ Collects the string passed on from both the Book ID and Memeber ID Entry boxes alongside the current date in dd/mm/yyyy format passed to the checkout date parameter and the Textbox from the GUI that contains the message
        
        The sql statement will first retrieve all the rows where both the checkout and return dates are full. Then it removes all the books with a book ID that has already been checked out.
        
        The result is either an empty or a full tuple, if full it inserts a whole new column with the Book ID, Member ID and Checkout Date. If empty, it would return a message that states that the Book ID entered is a book that is checked out already."""

        query1 = "SELECT *, ID FROM loan INNER JOIN book ON loan.Book_ID=ID WHERE ((Checkout_Date IS NOT NULL AND Return_Date IS NOT NULL) AND Book_ID=10) AND ID NOT IN (SELECT loan.Book_ID FROM loan WHERE (Checkout_Date IS NOT NULL AND Return_date IS NULL) ORDER BY Member_ID DESC) ORDER BY Member_ID DESC LIMIT 1".format(book_id)
        self.cur.execute(query1)
        rows = self.cur.fetchall()
        if len(rows) > 0:
            query2 = "INSERT INTO loan (BOOK_ID, Checkout_Date, Member_ID) VALUES ({},{},{})".format(book_id,checkout_date,member_id)
            self.cur.execute(query2)
            message.delete("1.0",END)
            message.insert(END,"Checkout of Book is Successful!!!!")
        else:
            message.delete("1.0",END)
            message.insert(END,"Book could not be checkout as someone is already using it")

    def add_return(self,book_id="",return_date="",member_id="",message=""):
        """ Collects the string passed on from both the Book ID and Memeber ID Entry boxes alongside the current date in dd/mm/yyyy format passed to the return date parameter and the Textbox from the GUI that contains the message
        
        The sql statement will first retrieve all the rows where both the checkout date is filled in and the return date has a null value. 
        
        The result is either an empty or a full tuple, if full it updates the row that has the empty column with the current date passed by return date on the condition that the same member checked out the book originally. If empty, it would return a message that states that the Book ID entered is a book that is still in the library."""
        
        query1 = "SELECT * FROM loan WHERE (Checkout_Date IS NOT NULL AND Return_Date IS NULL) AND (Book_ID={} AND Member_ID={}) ORDER BY Member_ID DESC".format(book_id,member_id)
        self.cur.execute(query1)
        rows = self.cur.fetchall()
        if len(rows) > 0:
            query2 = "UPDATE loan SET Return_Date = {} WHERE (Member_ID={} AND Book_ID = {})".format(return_date,member_id,book_id)
            self.cur.execute(query2)
            message.delete("1.0",END)
            message.insert(END,"Return of Book is Successful!!!!")
        else:
            message.delete("1.0",END)
            message.insert(END,"Ooops, it seems this book is still in the library please look at the list of books checked out and try again")

    def delete(self):
        """ Removes all the rows from both book and loan tables"""
        self.cur.execute("DELETE FROM book")
        self.cur.execute("DELETE FROM loan")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    if __name__ == "__main__":
        print(view)
        print("Extraction of all rows in book is successful")
        
        print(view_available_books)
        print("Extraction of all book that are available in the library is successful")

        print(view_checkedOut_books)
        print("Extraction of all books that are loaned out is successful")
