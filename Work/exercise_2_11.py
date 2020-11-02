'''
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
In order to generate the above report, you’ll first want to collect all of the data shown in the table. Write a function make_report() that takes a list of 
stocks and dictionary of prices as input and returns a list of tuples containing the rows of the above table.
'''

import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            stock = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(stock)
    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices
    

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

def make_report(portfolio,prices):
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = stock['name'],stock['shares'],current_price, change
        rows.append(summary)
    return rows

report = make_report(portfolio,prices)
headers = ('Name', 'Shares', 'Price', 'Change')

print('%10s %10s %10s %10s' % headers)
print(('-'*10 + ' ') * len(headers))
for r in report:
    print('%10s %10d %10.2f %10.2f' % r)

# otra forma:
'''
print('Alternative:')

for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
'''