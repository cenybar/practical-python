'''
Write a function read_prices(filename) that reads a set of prices such as this into a dictionary where the keys of the dictionary are the stock names and the 
values in the dictionary are the stock prices.
To do this, start with an empty dictionary and start inserting values into it just as you did above. However, you are reading the values from a file now.
We’ll use this data structure to quickly lookup the price of a given stock name.
A few little tips that you’ll need for this part. First, make sure you use the csv module just as you did before—there’s no need to reinvent the wheel here.

The other little complication is that the Data/prices.csv file may have some blank lines in it. Notice how the last row of data above is an empty list—meaning 
no data was present on that line.
There’s a possibility that this could cause your program to die with an exception. Use the try and except statements to catch this as appropriate. 
Thought: would it be better to guard against bad data with an if-statement instead?
Once you have written your read_prices() function, test it interactively to make sure it works:
prices = read_prices('Data/prices.csv')
prices['IBM']
106.28
'''
import csv

def read_prices(filename):
    portfolio = {}
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            try:
                portfolio[row[0]] = row[1]
            except IndexError:
                pass

    return portfolio