# Programmed by student F219244 on 14/11/2022

from tkinter import * 
from bookSearch import *
from bookCheckout import *
from bookReturn import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from bookSelect import *

window=Tk()
window.wm_title("Virtual Libranian Assistant")

def validate(action,index,value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
    """ Restrict the entry boxes of member ID and book ID to only allow numbers to fully register in the Box"""
    if(action=='1'):
        if text in '0123456789.-+':
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False
    else:
        return True 

# Naming the labels seen in the app
l1 = Label(window,text="Title")
l1.grid(row=0,column=0)

l2 = Label(window,text="Book ID")
l2.grid(row=0,column=2)

l3 = Label(window,text="Member ID")
l3.grid(row=1,column=0)

# Assigning the values of the input boxes 
title_text = StringVar()
e1 = Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

vcmd = (window.register(validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

bookID_text = StringVar()
e2 = Entry(window,textvariable=bookID_text, validate= 'key', validatecommand=vcmd)
e2.grid(row=0,column=3)

memberID_text = StringVar()
e3 = Entry(window,textvariable=memberID_text, validate= 'key', validatecommand=vcmd)
e3.grid(row=1,column=1)

#Generating the list box that will contain specific data depending on which button is pressed
list1 = Listbox(window, height=15, width=80)
list1.grid(row=2,column=0,rowspan=6,columnspan=2,padx=1,pady=20,sticky='e')

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6,sticky='nsw',pady=20)

# Generating the message box that will help guide the librarian on how to interact with the GUI
message_box = Text(window, height = 15, width = 100)
message_box.grid(row=8,column=1,pady=2)
message_box.insert(END,"Welcome to Virtual Librarian Assistant, Let's get started first with clicking the 'View All' button")

def open_popup():
    ''' This function collects the Matplotlib graph from bookSelect and places it in this pop up window'''
    top = Toplevel(window)
    top.geometry("1000x700")
    top.title("Book Analysis")
    fig = create_charts()
    canvas = FigureCanvasTkAgg(fig, master = top)
    canvas.draw()
    canvas.get_tk_widget().place(x=10, y=10)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',lambda:get_selected_row(e1,list1))

# Generating and assigning functionalities to all the buttons available on the GUI

b1a = Button(window,text="View All",width=20,command=lambda:view_command(list1,message_box))
b1a.grid(row=1,column=5)

b1b= Button(window,text="List of Books Checked Out",width=20,command=lambda:view_checked_books(list1))
b1b.grid(row=2,column=5)

b1c= Button(window,text="List of Available Books",width=20,command=lambda:view_available_books(list1))
b1c.grid(row=2,column=3)

b2 = Button(window,text="Search Book",width=20,command=lambda:search_command(list1,title_text))
b2.grid(row=3,column=5)

b3 = Button(window,text="Checkout Book",width=20,command=lambda:checkout_command(memberID_text,bookID_text,message_box))
b3.grid(row=4,column=5)

b4 = Button(window,text="Return Book",width=20,command=lambda:return_command(memberID_text,bookID_text,message_box))
b4.grid(row=5,column=5)

b5 = Button(window,text="Book Recommendation",width=20,command=open_popup)
b5.grid(row=6,column=5)


b6 = Button(window,text="Reset Library Database",width=20,command=lambda:reset_command(list1),fg="orange")
b6.grid(row=7,column=5)

b7 = Button(window,text="Close",width=20,command=window.destroy,fg="red")
b7.grid(row=8,column=5)

window.mainloop()
