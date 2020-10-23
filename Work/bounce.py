# bounce.py
#
# Exercise 1.5

height = 100
bounce = 3/5
count = 0

while count < 10:
    height = round(height*bounce,4)
    count += 1
    print(height)