# mortgage.py
#
# Exercise 1.9

'''
Modify the program so that extra payment information can be more generally handled. Make it so that the user can set these variables:

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

Make the program look at these variables and calculate the total paid appropriately.

How much will Dave pay if he pays an extra $1000/month for 4 years starting in year 5 of the mortgage?
'''
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra_payment_start_month = 61
extra_payment_end_month = 109
extra_payment = 1000


while principal > 0:
        if months >= extra_payment_start_month and months < extra_payment_end_month:
                principal = principal * (1+rate/12) - payment - extra_payment 
                total_paid = total_paid + payment + extra_payment
                months += 1
        else: 
                principal = principal * (1+rate/12) - payment 
                total_paid = total_paid + payment
                months += 1 
                

print('Total payment of {0} over {1} months.'.format(round(total_paid,2),months))


