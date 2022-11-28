# Programmed by student F219244 on 14/11/2022

from tkinter import END
from database import Database
import pandas as pd
from bookCheckout import loan_info


database = Database("Library.db")

def get_selected_row(event,e1,list1):
    """ When a book is clickes it extracts the necessary info from it """
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
    except IndexError:
        pass

def view_command(list1,message):
    """ This function removes the message already in the Text box, replaces it with appropriate text and then inserts all the rows of Book Information found in Book_Info.txt from the database into the List box."""
    message.delete("1.0",END)
    message.insert(END,"To search for your desired, first type title of the book in the title box and then click on the 'Search Book' button")
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

def search_command(list1,title_text):
    """ 
    Returns a list filled with rows that consist of a title that contains the String typed in the Title Entry Box
    """
    list1.delete(0,END)
    for row in database.search(title_text.get()):
        list1.insert(END,row)

def reset_command(list1):
    """ Deletes all the rows of data from both book and loan tables in the database and reinsert the original values from the two text files consisting of Book_Info.txt and Loan_Reservation.txt into the two database tables"""
    database.delete()
    loan_info()
    table_columns = ['ID','Genre','Title','Author','Purchase_price','Purchase_date']
    book_info = pd.read_csv('Book_Info.txt', sep=",", names=table_columns, header=None, index_col=False)
    for i in range(0,100):
        id_number = book_info['ID'].tolist()[i]
        genre = book_info['Genre'].tolist()[i]
        title = book_info['Title'].tolist()[i]
        author = book_info['Author'].tolist()[i]
        purchase_price = book_info['Purchase_price'].tolist()[i]
        purchase_date = book_info['Purchase_date'].tolist()[i]
        database.insert(id_number,genre,title,author,purchase_price,purchase_date)
        list1.delete(0,END)
        list1.insert(END,{id_number,genre,title,author,purchase_price,purchase_date})


