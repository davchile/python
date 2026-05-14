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
"""
# float → another type of data (number with a decimal) with function round included. It shows result always with decimals and commas as separator. Conditionals are needed if we want to show int numbers without decimals.
x = float(input("What's x? "))
y = float(input("What's y? "))

# print(f"{round(x + y, 2):,}") # this line shows the result and its decimals, then rounds it and put a comma the separate digits

# z = round(x + y) # rounds the result

# print(f"{z:,}") # put a comma to separate digits

# division and round with two digits
z = round(x / y, 2)

print(z)

# but if I want to use a format string. Here I am separating digits and having two decimals using format string.
z = x / y

print(f"{z:,.2f}")
"""
# getting a return value and using main()
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n): #generically n, this can be anything I want
    #return n * n

# another way to solve the math
    #return n ** 2 # the two asterisks raises "n" to the power of "2"

# and another way to solve the math
    return pow(n, 2) # this function has to arguments: the number and the exponent
main()