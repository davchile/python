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

print(f"{round(x + y, 2):,}")