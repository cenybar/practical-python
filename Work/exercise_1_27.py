with open('Data/portfolio.csv', 'rt') as f:
    next(f)
    myresults = []
    for line in f:
        row = line.split(',')
        shares = float(row[1])
        price = float(row[2])
        value = shares*price
        myresults.append(value)
    print('Total cost',sum(myresults))

    
    #shares = float(row[1])
    #price = float(row[2])
    #print(shares*price)

