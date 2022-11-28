# Programmed by student F219244 on 14/11/2022

from database import Database
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

# passes the tables from the Library Databases and creates a Dataframe that has all the views of the original 
# text files with the ids from both tables matching each other. 

conn = sqlite3.connect('Library.db')
query = conn.execute("SELECT * FROM book INNER JOIN loan ON book.ID = loan.Book_ID")
cols = [column[0] for column in query.description]
book_info = pd.DataFrame.from_records(data=query.fetchall(),columns = cols)

def create_charts():
    ''' Return a figure that contains two bar graph subplots. The first one counts how many times Genre is counted acrossed the Dataframe and the second one counts how many an individual book has been mentioned'''
    fig = plt.figure(figsize=(8,7))
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2)
    Top_Genre_Popularity = book_info.groupby('Genre')['ID'].count().sort_values(ascending=False)
    Top_Book_Popularity = book_info.groupby('Title')['ID'].count().sort_values(ascending=False).iloc[0:20]
    ax1.barh(Top_Genre_Popularity.index, Top_Genre_Popularity.values)
    ax1.set_title("Most Popular Library Genre ranked from Lowest to Highest")
    ax2.barh(Top_Book_Popularity.index, Top_Book_Popularity.values)
    ax2.set_title("Top 20 Most Popular Book of the Library")
    fig.tight_layout() 
    return fig

if __name__ == "__main__":    
    print(book_info.groupby('Title')['ID'].count().sort_values(ascending=False).iloc[0:20])
    print("Printing a index-value pair of each individual book is successful")

    print(book_info.groupby('Genre')['ID'].count().sort_values(ascending=False))
    print("Printing a index-value pair of each genre is successful")

    print(book_info.groupby('Title')['ID'].count().sort_values(ascending=False).iloc[0:20].values)
    print("Extraction of values of the index-value pair of each individual book is successful")

    print(book_info.groupby('Title')['ID'].count().sort_values(ascending=False).iloc[0:20].index)
    print("Extraction of indexes of the index-value pair of each individual book is successful")