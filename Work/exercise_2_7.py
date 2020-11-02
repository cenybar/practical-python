'''
Tie all of this work together by adding a few additional statements to your report.py program that computes gain/loss. These statements should take the list of 
stocks in Exercise 2.5 and the dictionary of prices in Exercise 2.6 and compute the current value of the portfolio along with the gain/loss.
'''
import csv

def read_prices(filename):
    stocks = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                stocks[row[0]] = row[1]
            except IndexError:
                pass

    return stocks

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)

    return portfolio

prices = read_prices('Data/prices.csv')
portfolio = read_portfolio('Data/portfolio.csv')

valuation = []
new_valuation = []
for row in portfolio:
    stock,price,amount = row
    value = price*amount
    new_price = float(prices[stock])
    new_value = new_price*amount
    valuation.append(value)
    new_valuation.append(new_value)


print('Portfolio previous value: ',sum(valuation))
print('Portfolio current value: ',round(sum(new_valuation),2))
print('Gain/loss: ', round(-sum(valuation)+sum(new_valuation),2))

# Calculate the total cost of the portfolio
total_cost = 0.0
for s in portfolio:
    total_cost += s['shares']*s['price']

print('Total cost', total_cost)

# Compute the current value of the portfolio
total_value = 0.0
for s in portfolio:
    total_value += s['shares']*prices[s['name']]

print('Current value', total_value)
print('Gain', total_value - total_cost)
