# mortgage.py
#
# Exercise 1.8
'''
Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?

Modify the program to incorporate this extra payment and have it print the total amount paid along with the number of months required.

When you run the new program, it should report a total payment of 929,965.62 over 342 months.
'''

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra = 1000


while principal > 0:
        if months < 12:
                principal = principal * (1+rate/12) - payment - extra 
                total_paid = total_paid + payment + extra
                months += 1
        else: 
                principal = principal * (1+rate/12) - payment 
                total_paid = total_paid + payment
                months += 1 
                

print('Total payment of {0} over {1} months.'.format(round(total_paid,2),months))

