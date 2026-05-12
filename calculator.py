""" First try
x = input("What's x? ")
y = input("What's y? ")

z= int(x) + int(y)

print(z)
"""

""" it seems to be shorter
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)
"""

# float → another type of data (number with a decimal) with function round included. It shows result always with decimals and commas as separator. Conditionals are needed if we want to show int numbers without decimals.
x = float(input("What's x? "))
y = float(input("What's y? "))

# print(f"{round(x + y, 2):,}") # this line shows the result and its decimals, then rounds it and put a comma the separate digits

# z = round(x + y) # rounds the result

# print(f"{z:,}") # put a comma to separate digits

# division and round with two digits
"""z = round(x / y, 2)

print(z)
"""
# but if I want to use a format string
z = x / y

print(f"{z:,.2f}")


