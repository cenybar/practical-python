# mortgage.py
#
# Exercise 1.10

'''
Modify the program to print out a table showing the month, total paid so far, and the remaining principal. The output should look something like this:

1 2684.11 499399.22
2 5368.22 498795.94
3 8052.33 498190.15
4 10736.44 497581.83
5 13420.55 496970.98
...
308 874705.88 3478.83
309 877389.99 809.21
310 880074.1 -1871.53
Total paid 880074.1
Months 310

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
                print(months,total_paid,principal)
                principal = principal * (1+rate/12) - payment - extra_payment 
                total_paid = total_paid + payment + extra_payment
                months += 1
        else: 
                print(months,total_paid,principal)
                principal = principal * (1+rate/12) - payment 
                total_paid = total_paid + payment
                months += 1 
                
print(months,total_paid,principal)
print('Total payment of {0} over {1} months.'.format(round(total_paid,2),months))


